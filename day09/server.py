from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import AIAgent  # This line works because ai_agent.py is in the same folder!

# 1. Boot up the FastAPI app
app = FastAPI()

# 2. Boot up the AI Agent (Global state so memory persists between web requests)
web_agent = AIAgent(
    name="WebScout", 
    system_prompt="You are a helpful AI backend. Keep answers strictly under 2 sentences."
)

# 3. Define the strict Data Model using Pydantic
class UserInput(BaseModel):
    message: str

# 4. The POST Endpoint
@app.post("/api/chat")
def chat_with_ai(payload: UserInput):
    # Step A: Extract the string from the JSON payload
    user_text = payload.message
    
    # Step B: Inject it into the AI's memory
    web_agent.add_to_memory("user", user_text)
    
    # Step C: Trigger the API call and catch the returned response
    ai_response = web_agent.ask_llm()
    
    # Step D: Send the JSON response back to the client (the web browser)
    return {
        "agent_name": web_agent.name,
        "user_message": user_text,
        "ai_reply": ai_response
    }