import os

OUTPUT_DIR = "playwright_tests"


def generate_test_code(scenario_name: str, structured_steps: list) -> str:
    lines = []
    lines.append("from playwright.sync_api import Page, expect")
    lines.append("")
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
