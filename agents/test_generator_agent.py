
OUTPUT_DIR = "playwright_tests"


def generate_test_code(scenario_name: str, structured_steps: list) -> str:
    """
    Converts structured test steps into a Playwright test function.
    Always produces a syntactically correct test file.
    """
    lines = []
    lines.append("from playwright.sync_api import Page, expect")
    lines.append("")

    # Function name, clean and safe
    func_name = f"test_{scenario_name.replace(' ', '_').lower()}"
    lines.append(f"def {func_name}(page: Page):")

    if not structured_steps:
        # Always valid Python
        lines.append
