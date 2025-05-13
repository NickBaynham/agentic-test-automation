import requests
r = requests.post("http://192.168.68.51:11434/api/generate", json={
    "model": "mistral",
    "prompt": "Say hello",
    "stream": False
})
print(r.json()["response"])

