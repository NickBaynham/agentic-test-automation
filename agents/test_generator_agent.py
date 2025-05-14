import os
import requests
import json

OLLAMA_URL = "http://192.168.68.51:11434/api/generate"
MODEL = "codellama:7b"
OUTPUT_DIR = "playwright_tests"


def generate_test_code(scenario_name: str, structured_steps: list) -> str:
    slug = scenario_name.replace(" ", "_").lower()

    prompt = f"""
You are an AI assistant that writes Python tests using Playwright and pytest.

Write a test function named test_{slug}. The function should:
- Use the sync API from Playwright
- Include only these imports: from playwright.sync_api import Page, expect
- Accept a `page: Page` parameter
- Avoid using `playwright.chromium.launch()` or `with page:`
- Do NOT include page.close(), pytest imports, or setup code — assume `page` is a fixture
- Only output valid Python code, no explanations

Structured test steps:
{json.dumps(structured_steps, indent=2)}

Only output the complete Python code for the test function.
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })

        result = response.json()["response"].strip()
        print(f"🧠 LLM generated code for: {scenario_name}\n")
        return result

    except Exception as e:
        print(f"❌ Code generation failed: {e}")
        return f"from playwright.sync_api import Page\n\ndef test_{slug}(page: Page):\n    pass  # generation failed"


def save_test_file(filename: str, code: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    print(f"✅ Test code saved to {path}")
