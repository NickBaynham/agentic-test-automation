import requests

OLLAMA_URL = "http://192.168.68.51:11434/api/generate"

prompt = """
You are a JSON API. Extract structured test step info from the following instruction:

"Click on the 'Submit' button"

Respond only with a valid JSON object in this format:

{
  "action": "click",
  "target": "Submit",
  "data": null
}

Do not include any extra explanation or text.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "mistral",
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
