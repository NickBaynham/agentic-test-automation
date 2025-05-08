import uuid
import re


def parse_step_simple(step_text):
    if isinstance(step_text, str):
        text = step_text.lower()

        if not text:
            return {
                "id": str(uuid.uuid4()),
                "raw": step_text,
                "action": "unknown",  # placeholder for more advanced parsing
                "target": "unknown",
                "data": None
            }
        if "navigate to" in text:
            action = "navigate"
            target = text.split("navigate to")[-1].strip()
            data = None

        elif "click" in text:
            action = "click"
            # crude selector guess from phrasing
            target = text.split("click on")[-1].strip() if "click on" in text else "button"
            data = None

        elif "type" in text or "enter" in text:
            action = "type"
            target = "editor"
            # extract the text inside quotes
            match = re.search(r'["“](.*?)["”]', step_text)
            data = match.group(1) if match else "example text"

        else:
            action = "unknown"
            target = "unknown"
            data = None

        return {
            "id": str(uuid.uuid4()),
            "raw": step_text,
            "action": action,
            "target": target,
            "data": data
        }
    else:
        return {
            "id": str(uuid.uuid4()),
            "raw": step_text,
            "action": "unknown",  # placeholder for more advanced parsing
            "target": "unknown",
            "data": None
        }


def parse_step_demo(step_text):
    """Convert raw text step into a structured dict."""
    return {
        "id": str(uuid.uuid4()),
        "raw": step_text,
        "action": "unknown",  # placeholder for more advanced parsing
        "target": "unknown",
        "data": None
    }


def plan_test(scenario):
    print(f"\n🧠 [PlannerAgent] Planning test for: {scenario.get('scenario')}")

    steps = scenario.get("steps", [])
    print(len(steps), " steps")
    structured_steps = [parse_step_simple(step) for step in steps]

    print(f"📋 Planned {len(structured_steps)} structured steps.")
    return structured_steps
