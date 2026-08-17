import os
from dotenv import load_dotenv

# 1. Load the hidden variables from the .env file into the OS
load_dotenv()

# 2. Retrieve the key safely
my_key = os.getenv("GROQ_API_KEY")

# 3. HTTP Headers (The VIP Pass)
# When sending data to an AI, you must attach 'Headers' to prove who you are.
headers = {
    "Authorization": f"Bearer {my_key}",
    "Content-Type": "application/json"
}

# 4. HTTP POST (Sending data)
# GET requests just download. POST requests SEND data and get a response.
# payload = {"model": "llama3", "messages": [{"role": "user", "content": "Hi"}]}
# response = requests.post(url, headers=headers, json=payload)