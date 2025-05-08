import subprocess
import os


def run_playwright_tests(test_dir="playwright_tests"):
    print(f"🧪 [ExecutorAgent] Running tests in {test_dir}...")

    if not os.path.exists(test_dir):
        print(f"❌ Test directory '{test_dir}' not found.")
        return

    # Run pytest on the directory
    try:
        result = subprocess.run(
            ["pdm", "run", "pytest", test_dir],
            capture_output=True,
            text=True,
            check=False
        )

        print("📤 Test Output:\n")
        print(result.stdout)
        if result.stderr:
            print("⚠️ Test Errors:\n")
            print(result.stderr)

    except Exception as e:
        print(f"❌ Failed to execute tests: {e}")
