import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class AIAgent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        self.api_key = os.getenv("GROQ_API_KEY")
        
        # FIX 1: Strict API Schema (role and content only)
        self.memory = [{"role": "system", "content": self.system_prompt}]

    def add_to_memory(self, role, content):
        # FIX 2: No square brackets inside append
        self.memory.append({"role": role, "content": content})

    def fetch_external_data(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                print("✓ Raw data successfully fetched from internet.")
                return data  # FIX 3: Actually return the data!
            else:
                print(f"Failed to fetch. Status: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            return None

    def ask_llm(self):
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",  # Updated to the working model
            "messages": self.memory
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                ai_reply = response.json()["choices"][0]["message"]["content"]
                print(f"\n[{self.name} SUMMARY]:\n{ai_reply}\n")
                self.add_to_memory("assistant", ai_reply)
            else:
                print(f"\nAPI Error {response.status_code}: {response.text}\n")
        except requests.exceptions.RequestException as e:
            print(f"Network failure: {e}")

    def save_agent_state(self):
        filename = f"{self.name}_memory.json"
        with open(filename, "w") as file:
            json.dump(self.memory, file, indent=4)
        print(f"✓ Session saved to {filename}")

# ==========================================
# MAIN EXECUTION: THE AUTONOMOUS SCOUT
# ==========================================
if __name__ == "__main__":
    # 1. Boot up the agent
    scout = AIAgent(
        name="DataScout", 
        system_prompt="You are an expert research analyst. Summarize raw data concisely in bullet points."
    )

    # 2. Fetch target data from the internet
    print("Fetching target data...")
    raw_post = scout.fetch_external_data("https://jsonplaceholder.typicode.com/posts/3")

    # 3. If fetch was successful, inject it into the AI's memory and ask for a summary
    if raw_post:
        prompt = f"Please analyze and summarize this raw JSON data: {raw_post}"
        scout.add_to_memory("user", prompt)
        
        print("Sending to LLM for analysis...")
        scout.ask_llm()

    # 4. Save the entire process to the hard drive
    scout.save_agent_state()