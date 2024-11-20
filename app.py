from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from model import *

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(chat_request: ChatRequest):
    user_message = chat_request.message
    bot_response = chat(query_engine,user_message)
    return {"response": bot_response}

if __name__ == "__main__":
    init_llm()
    index = init_index(Settings.embed_model)
    query_engine = init_query_engine(index)
    uvicorn.run(app, host="0.0.0.0", port=8000)