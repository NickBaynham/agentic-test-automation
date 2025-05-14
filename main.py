from agents.test_executor_agent import run_playwright_tests
from agents.test_generator_agent import ai_generate_test_code, save_test_file
from scenario_loader import load_scenarios
from agents.test_planner_agent import plan_test
import json


def run_agentic_workflow(scenario):
    scenario_name = scenario.get('scenario', 'UnnamedScenario')
    print(f"\n🚀 Generating Script for Scenario: {scenario_name}")

    # Step 1: Planner Agent → Structure raw steps
    structured_steps = plan_test(scenario)
    for step in structured_steps:
        print(step)

    # Step 2: Generator Agent → Convert structured steps to Playwright code
    code = ai_generate_test_code(scenario_name, structured_steps)
    print(code)

    # Step 3: Save to file
    filename = f"test_{scenario_name.replace(' ', '_').lower()}.py"
    save_test_file(filename, code)


def main():
    print("📦 Loading scenarios...")
    scenarios = load_scenarios()

    if not scenarios:
        print("❌ No scenarios found in /scenarios/")
        return
    else:
        print(len(scenarios), "scenarios found and added.")

    for scenario in scenarios:
        print(json.dumps(scenario["data"], indent=2))
        run_agentic_workflow(scenario["data"])

    print("\n✅ All scenarios processed. Playwright tests generated in /playwright_tests/\n")
    run_playwright_tests()


if __name__ == "__main__":
    main()
