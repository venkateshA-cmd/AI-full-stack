from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class UserInput(BaseModel):
    username:str
    prompt:str

@app.post("/chat")

def chat_endpoint(request_data:UserInput):
    

    name = request_data.username
    text = request_data.prompt

    return {
        "message":f"Hello{name},I recieved your prompt:{text}"
    }