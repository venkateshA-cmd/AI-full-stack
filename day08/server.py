from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

# Endpoint 1: Health Check
@app.get("/")
def home():
    return {"status": "active", "version": "1.0.0"}

# Endpoint 2: Dynamic Path Parameter
# Notice the {keyword} in the route! This tells FastAPI to grab whatever 
# the user types in the URL and pass it into the function.
@app.get("/analyze/{keyword}")
def dynamic(keyword: str):
    # We do NOT use input()! 
    # If the user visits http://127.0.0.1:8000/analyze/crypto
    # The 'keyword' variable automatically becomes "crypto".
    
    return {
        "task": "analysis", 
        "target_keyword": keyword, 
        "result": "Fake analysis complete"
    }