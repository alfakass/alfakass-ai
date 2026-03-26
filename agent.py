import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

INFERENCE_ENDPOINT = os.getenv("INFERENCE_ENDPOINT")
API_KEY = os.getenv("GITHUB_API_KEY")
MODEL = os.getenv("MODEL")

def chat_with_model(prompt: str) -> str:
    conversation_history = [
        {
            "role": "user",
            "content": "You are a helpful assistant.",
        }
    ]

    user_message = {
        "role": "user",
        "content": prompt
    }

    conversation_history.append(user_message)

    client = OpenAI(base_url=INFERENCE_ENDPOINT, api_key=API_KEY)

    response = client.chat.completions.create(
        messages = conversation_history,
        model = MODEL,
    )

    return response.choices[0].message.content


