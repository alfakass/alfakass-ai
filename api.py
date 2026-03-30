import uvicorn
from fastapi import FastAPI
from assistant import chat_with_model
from models.chat import ChatRequest
from rag import embed_documents
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Setting Up Application")
    print("Embedding Documents")
    embed_documents()
    print("Done Embedding Documents")

    yield
    print("Shutting Down Application")

app = FastAPI(lifespan=lifespan)

@app.post("/chat")
async def chat(request_body: ChatRequest):
    return chat_with_model(query=request_body.prompt)

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
