import requests


def generate_response(prompt):
    url = "http://localhost:11434//api/generate"
    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    data = response.json()
    llm_response = data.get("response", "No response found in the API response")
    return llm_response
