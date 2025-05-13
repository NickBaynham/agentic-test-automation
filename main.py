from scenario_loader import load_scenarios
from agents.test_planner_agent import plan_test


def run_agentic_test(scenario):
    scenario_name = scenario.get('scenario', 'UnnamedScenario')
    print(f"\n🚀 Running Scenario: {scenario_name}")

    # Step 1: Planner Agent → Structure raw steps
    structured_steps = plan_test(scenario)
    print(structured_steps)

    # Step 2: Generator Agent → Convert structured steps to Playwright code
    # code = generate_test_code(scenario_name, structured_steps)
    # print(code)

    # Step 3: Save to file
    # filename = f"test_{scenario_name.replace(' ', '_').lower()}.py"
    # save_test_file(filename, code)


def main():
    print("📦 Loading scenarios...")
    scenarios = load_scenarios()

    if not scenarios:
        print("❌ No scenarios found in /scenarios/")
        return
    else:
        print(len(scenarios), "scenarios found and added.")

    for scenario_file in scenarios:
        run_agentic_test(scenario_file["data"])

    print("\n✅ All scenarios processed. Playwright tests generated in /playwright_tests/\n")
    # run_playwright_tests()


if __name__ == "__main__":
    main()
