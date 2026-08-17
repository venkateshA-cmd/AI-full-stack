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
        
        # Strict API Schema (role and content only)
        self.memory = [{"role": "system", "content": self.system_prompt}]

    def add_to_memory(self, role, content):
        self.memory.append({"role": role, "content": content})

    def fetch_external_data(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException:
            return None

    def ask_llm(self):
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",  # The current working model
            "messages": self.memory
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                ai_reply = response.json()["choices"][0]["message"]["content"]
                
                # Save the AI's reply to the agent's memory
                self.add_to_memory("assistant", ai_reply)
                
                # NEW: Return the reply so the web server can send it to the browser!
                return ai_reply
            else:
                error_msg = f"API Error {response.status_code}: {response.text}"
                return error_msg
                
        except requests.exceptions.RequestException as e:
            return f"Network failure: {e}"

    def save_agent_state(self):
        filename = f"{self.name}_memory.json"
        with open(filename, "w") as file:
            json.dump(self.memory, file, indent=4)