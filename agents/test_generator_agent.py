import os

OUTPUT_DIR = "playwright_tests"


def generate_test_code(scenario_name: str, structured_steps: list) -> str:
    """
    Converts structured test steps into a Playwright test function.
    """

    lines = []
    lines.append("from playwright.sync_api import Page, expect")
    lines.append("")
    lines.append(f"def test_{scenario_name.replace(' ', '_').lower()}(page: Page):")

    if not structured_steps:
        lines.append("    pass  # No steps defined")
        return "\n".join(lines)

    # for step in structured_steps:
    #     raw = step.get("raw", "").lower()
    #
    #     # Basic keyword-based action translation
    #     if "navigate to" in raw:
    #         url = raw.split("navigate to")[-1].strip()
    #         lines.append(f"    page.goto('{url}')")
    #
    #     elif "click" in raw:
    #         target = step.get("target", "unknown")
    #         lines.append(f"    page.click('text={target}')  # TODO: improve selector")
    #
    #     elif "type" in raw or "enter" in raw:
    #         content = step.get("data", "example text")
    #         lines.append(f"    page.keyboard.type('{content}')")
    #
    #     else:
    #         lines.append(f"    # TODO: handle step: {raw}")

    return "\n".join(lines)


def save_test_file(filename: str, code: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, "w") as f:
        f.write(code)

    print(f"✅ Test code saved to: {file_path}")
