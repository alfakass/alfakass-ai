import uvicorn
from fastapi import FastAPI
from assistant import chat_with_model
from models.chat import ChatRequest

app = FastAPI()

@app.post("/chat")
async def chat(request_body: ChatRequest):
    return chat_with_model(prompt=request_body.prompt)

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
