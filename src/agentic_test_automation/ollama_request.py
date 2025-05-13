import requests

OLLAMA_URL = "http://192.168.68.51:11434/api/generate"
response = requests.post(
    OLLAMA_URL,
    json={
        "model": "mistral",
        "prompt": "Extract action, target, data from: Click on the 'Submit' button",
        "stream": False
    }
)

print(response.json()["response"])
