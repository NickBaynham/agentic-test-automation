from scenario_loader import load_scenarios
from agents.test_planner_agent import plan_test


def run_agentic_test(scenario):
    print(f"\n🚀 Running Scenario: {scenario.get('scenario')}")
    structured_steps = plan_test(scenario)

    print("🧱 Structured Steps:")
    for step in structured_steps:
        print(f" - {step['raw']} → action: {step['action']} | target: {step['target']}")

    # TODO: pass to GeneratorAgent next
    print("🤖 Planner complete.\n")


def main():
    print("📦 Loading scenarios...")
    scenarios = load_scenarios()

    if not scenarios:
        print("❌ No scenarios found in /scenarios/")
        return

    for scenario_file in scenarios:
        run_agentic_test(scenario_file["data"])


if __name__ == "__main__":
    main()
