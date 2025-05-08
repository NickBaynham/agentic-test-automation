import os
import yaml

SCENARIO_DIR = "scenarios"


def load_scenarios():
    scenarios = []

    for filename in os.listdir(SCENARIO_DIR):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            filepath = os.path.join(SCENARIO_DIR, filename)
            with open(filepath, 'r') as file:
                try:
                    scenario = yaml.safe_load(file)
                    scenarios.append({
                        "filename": filename,
                        "data": scenario
                    })
                except yaml.YAMLError as e:
                    print(f"❌ Error loading {filename}: {e}")

    return scenarios


# Example usage
if __name__ == "__main__":
    all_scenarios = load_scenarios()
    for s in all_scenarios:
        print(f"\n✅ Loaded: {s['filename']}")
        print(f"Scenario: {s['data'].get('scenario')}")
        print(f"Steps: {len(s['data'].get('steps', []))} defined\n")
