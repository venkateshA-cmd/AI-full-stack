from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {"status":"success","message":"welcome to my AI server!"}

