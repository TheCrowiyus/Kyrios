import requests

def transcribe_audio(file_path, language="en", url="http://localhost:8000/v1/audio/transcriptions"):
    try:
        with open(file_path, "rb") as file:
            files = {"file": file}
            data = {"language": language}
            response = requests.post(url, files=files, data=data)

        if response.ok:
            transcription = response.json().get("text", "")
            return transcription.strip()  # Remove surrounding spaces or newlines
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"




