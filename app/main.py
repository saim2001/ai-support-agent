from fastapi import FastAPI
from pydantic import BaseModel

from .agent import run_agent


app = FastAPI(title="AI Support Agent")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = run_agent(request.message)

    return ChatResponse(response=response)