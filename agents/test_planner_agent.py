import uuid


def parse_step(step_text):
    """Very simple NLP-style breakdown for proof-of-concept."""
    return {
        "id": str(uuid.uuid4()),
        "raw": step_text,
        "action": "unknown",  # placeholder for LLM/regex-based parsing
        "target": "unknown",
        "data": None
    }


def plan_test(scenario):
    print(f"\n🧠 [PlannerAgent] Planning test for: {scenario.get('scenario')}")

    steps = scenario.get("steps", [])
    structured_steps = [parse_step(step) for step in steps]

    print(f"📋 Planned {len(structured_steps)} structured steps.")
    return structured_steps
