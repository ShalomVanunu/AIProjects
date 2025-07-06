import requests
import json

url = "http://localhost:11434/api/chat"


payload = {
    "model": "mistral",
    "messages":[{"role":"user","content":"electric car one sentence"}]
}


response = requests.post(url, json=payload)

if response.status_code == 200 :
    for line in response.iter_lines():
        if line:
            json_data = json.loads(line)
            print(json_data["message"]["content"], end="")

