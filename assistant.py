import os
from openai import OpenAI
from dotenv import load_dotenv
from rag import get_similar_chunks

load_dotenv()

INFERENCE_ENDPOINT = os.getenv("INFERENCE_ENDPOINT")
API_KEY = os.getenv("GITHUB_API_KEY")
MODEL = os.getenv("MODEL")

def chat_with_model(query: str) -> str:
    conversation_history = [
        {
            "role": "user",
            "content": "You are a helpful assistant.",
        }
    ]

    chunks = get_similar_chunks(query)
    context = "\n\n".join(chunks)

    augmented_prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question: {query}
    """

    user_message = {
        "role": "user",
        "content": augmented_prompt
    }

    conversation_history.append(user_message)

    client = OpenAI(base_url=INFERENCE_ENDPOINT, api_key=API_KEY)

    response = client.chat.completions.create(
        messages = conversation_history,
        model = MODEL,
    )

    reply = response.choices[0].message.content

    assistant_message = {"role": "assistant", "content": reply}
    conversation_history.append(assistant_message)

    return reply


