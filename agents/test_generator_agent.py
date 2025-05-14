import os
import requests
import json

OLLAMA_URL = "http://192.168.68.51:11434/api/generate"  # Update IP for your network setup
MODEL = "codellama:7b"
OUTPUT_DIR = "playwright_tests"


def ai_generate_test_code(scenario_name: str, structured_steps: list) -> str:
    """
    Uses an LLM (like CodeLlama) via Ollama to generate Playwright test code
    based on structured steps.
    """
    print("AI Test Code Generation in Progress")
    slug = scenario_name.replace(" ", "_").lower()

    prompt = f"""
You are a Python test automation assistant.
Generate a Playwright test function in Python using pytest.
Scenario: {scenario_name}
Steps (structured):
{json.dumps(structured_steps, indent=2)}
Requirements:
- Use Playwright's sync API
- Add required imports
- The function must be named test_{slug}
- Use only valid Python syntax
- Output only the full code, nothing else
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })

        result = response.json()["response"]
        print(f"🧠 LLM generated code for: {scenario_name}\n")
        return result.strip()

    except Exception as e:
        print(f"❌ Code generation failed: {e}")
        return f"# Code generation failed for scenario: {scenario_name}\ndef test_{slug}(page: Page):\n    pass\n"


def generate_test_code(scenario_name: str, structured_steps: list) -> str:
    lines = ["from playwright.sync_api import Page, expect", ""]
    func_name = f"test_{scenario_name.replace(' ', '_').lower()}"
    lines.append(f"def {func_name}(page: Page):")

    if not structured_steps:
        lines.append("    pass  # No steps available")
        return "\n".join(lines)

    for step in structured_steps:
        action = step.get("action")
        target = step.get("target")
        data = step.get("data")
        raw = step.get("raw", "")

        if action == "navigate":
            lines.append(f"    page.goto('{target}')")

        elif action == "click":
            selector = f"text={target}" if target else "button"
            lines.append(f"    page.click('{selector}')")

        elif action == "type":
            lines.append(f"    page.keyboard.type('{data}')")

        elif action == "assert_title_contains":
            lines.append(f"    assert {target} in page.title().lower()")

        elif action == "assert_text_present":
            lines.append(f"    assert page.locator('body').inner_text().find('{target}') != -1")

        else:
            lines.append(f"    # TODO: Unhandled action: {action} from raw step: {raw}")

    return "\n".join(lines)


def save_test_file(filename: str, code: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    print(f"✅ Test code saved to {path}")
