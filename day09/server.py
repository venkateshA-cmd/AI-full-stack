from fastapi import FastAPI, Depends # NEW: Depends is for Dependency Injection
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session   # NEW: Session type for validation
from pydantic import BaseModel
from ai_agent import AIAgent

from database import engine, SessionLocal, Base
import models

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middleware (The Bouncer)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# Boot up the AI Agent
web_agent = AIAgent(
    name="WebScout", 
    system_prompt="You are a helpful AI backend. Keep answers strictly under 2 sentences."
)

class UserInput(BaseModel):
    message: str

# --- NEW: Database Session Manager ---
def get_db():
    db = SessionLocal()
    try:
        yield db  # Give the connection to the route
    finally:
        db.close() # Always close it, even if the code crashes!

# --- UPDATED: The POST Endpoint ---
# Notice we added 'db: Session = Depends(get_db)' to the function arguments!
@app.post("/api/chat")
def chat_with_ai(payload: UserInput, db: Session = Depends(get_db)):
    
    # 1. Extract user text
    user_text = payload.message
    
    # 2. Add to Agent Memory and ask LLM
    web_agent.add_to_memory("user", user_text)
    ai_response = web_agent.ask_llm()
    
    # 3. --- DATABASE INSERTION (The Magic!) ---
    # We create a new row using the Class we built in models.py
    new_chat_log = models.ChatHistory(
        agent_name=web_agent.name,
        user_message=user_text,
        ai_reply=ai_response
    )
    
    db.add(new_chat_log) # Stage the data
    db.commit()          # Actually save it to the hard drive!
    db.refresh(new_chat_log) # Refresh to get the generated ID
    
    # 4. Send the response back to the browser
    return {
        "db_id": new_chat_log.id, # We return the database ID as proof!
        "agent": web_agent.name,
        "user": user_text,
        "ai": ai_response
    }