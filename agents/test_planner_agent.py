import uuid
import re
import requests
import json

OLLAMA_URL = "http://192.168.68.51:11434/api/generate"
MODEL = "mistral"
prompt = """
You are a JSON API. Extract structured test step info from the following instruction:

"{step_text}"

Respond only with a valid JSON object in this format:

{
  "action": "click",
  "target": "Submit",
  "data": null
}

Do not include any extra explanation or text.
"""


def ai_parse_step(step_text):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    # Parse JSON safely
    try:
        result = response.json()["response"]
        print("🔁 Raw model response:\n", result)

        # Strip whitespace or unexpected formatting, if needed
        import json
        parsed = json.loads(result.strip())
        print("\n✅ Parsed JSON object:\n", parsed)

    except Exception as e:
        print(f"❌ Error parsing model response: {e}")

    return {
        "id": str(uuid.uuid4()),
        "raw": step_text,
        "action": parsed.get("action", "unknown"),
        "target": parsed.get("target", "unknown"),
        "data": parsed.get("data", None)
    }


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

        elif "verify" in text:
            action = "assert_title_contains"
            target = text.split("verify the title contains")[-1].strip()
            data = None
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
    print("The scenario contains", len(steps), "steps")
    structured_steps = [parse_step_simple(step) for step in steps]

    print(f"📋 Planned {len(structured_steps)} structured steps.")
    return structured_steps
