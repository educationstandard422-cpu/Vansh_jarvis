import os
import json
import urllib.request
import urllib.error

API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL = "gpt-5.6-mini"

def ask_ai(question):
    if not API_KEY:
        return (
            "JARVIS શરૂ થયો છે, પરંતુ AI API key હજુ સેટ નથી. "
            "પછી આપણે key setup કરીશું."
        )

    url = "https://api.openai.com/v1/chat/completions"

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are JARVIS, a personal AI assistant. "
                    "Be concise, helpful and accurate. "
                    "Support Gujarati, Hindi and English."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + API_KEY
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]

    except Exception as error:
        return "JARVIS error: " + str(error)


def main():
    print("=" * 40)
    print("        JARVIS AI ASSISTANT")
    print("=" * 40)
    print("Type 'exit' to stop.")

    while True:
        user = input("\nYou: ")

        if user.lower() in ["exit", "quit"]:
            print("JARVIS: Goodbye!")
            break

        if user.strip():
            answer = ask_ai(user)
            print("\nJARVIS:", answer)


if __name__ == "__main__":
    main()
