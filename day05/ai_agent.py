import requests
import json
import os
from dotenv import load_dotenv

# Load secret environment variables from the .env file
load_dotenv()

class AIAgent:
    # 1. THE CONSTRUCTOR
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        # Fixed the typo: api_key instead of api_ley
        self.api_key = os.getenv("GROQ_API_KEY") 
        # Start memory with the system prompt as the first entry
        self.memory = [{"role": "system", "content": self.system_prompt}]

    # 2. THE MEMORY MANAGER
    def add_to_memory(self, role, content):
        self.memory.append({"role": role, "content": content})

    # 3. THE EXTERNAL TOOL (GET Request)
    def fetch_external_data(self, url):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                raw_data = response.json() 
                print("✓ Data successfully fetched from server.")
                return raw_data 
            else:
                print(f"Error: Server responded with status {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Network failure: {e}")
            return None

    # 4. THE LLM INTEGRATION (POST Request)
    def ask_llm(self):
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama3-8b-8192",
            "messages": self.memory
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            
            if response.status_code == 200:
                ai_reply = response.json()["choices"][0]["message"]["content"]
                print(f"\n[{self.name}]: {ai_reply}\n")
                
                # Save the AI's reply to the agent's memory
                self.add_to_memory("assistant", ai_reply)
            else:
                print(f"\nAPI Error {response.status_code}: {response.text}\n")
                
        except requests.exceptions.RequestException as e:
            print(f"Network failure: {e}")

    # 5. THE DISK SAVER
    def save_agent_state(self):
        filename = f"{self.name}_memory.json"
        with open(filename, "w") as file:
            json.dump(self.memory, file, indent=4)
        print(f"✓ Agent state saved to {filename}")

# ==========================================
# MAIN EXECUTION (Day 6 Test)
# ==========================================

if __name__ == "__main__":
    # 1. Boot up the agent
    jarvis = AIAgent(name="Jarvis", system_prompt="You are a sarcastic AI assistant. Keep answers under 2 sentences.")

    # 2. Add user prompt
    jarvis.add_to_memory("user", "Why is the sky blue?")

    # 3. Call the AI!
    print("Thinking...")
    jarvis.ask_llm()

    # 4. Save state
    jarvis.save_agent_state()