import requests
import json

class AIAgent:
    # 1. THE CONSTRUCTOR
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        # Start memory with the system prompt as the first entry
        self.memory = [{"role": "system", "content": self.system_prompt}]

    # 2. THE MEMORY MANAGER
    def add_to_memory(self, role, content):
        # We use the temporary parameters 'role' and 'content' directly.
        # No need for self.role here!
        self.memory.append({"role": role, "content": content})

    # 3. THE EXTERNAL TOOL
    def fetch_external_data(self, url):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                raw_data = response.json() 
                print("✓ Data successfully fetched from server.")
                return raw_data  # Returns the data like a baton
            else:
                print(f"Error: Server responded with status {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Network failure: {e}")
            return None

    # 4. THE DISK SAVER
    def save_agent_state(self):
        # We dynamically name the file based on the agent's name
        filename = f"{self.name}_memory.json"
        
        with open(filename, "w") as file:
            # We dump the ACTUAL memory list into the file
            json.dump(self.memory, file, indent=4)
        print(f"✓ Agent state saved to {filename}")

# ==========================================
# MAIN EXECUTION
# ==========================================

# 1. Instantiate the object
scout = AIAgent(name="DataScout", system_prompt="You are a data gatherer.")

# 2. Add a user prompt
scout.add_to_memory("user", "Go fetch post number 1.")

# 3. Run the tool AND CATCH THE RETURNED DATA in a variable
fetched_data = scout.fetch_external_data("https://jsonplaceholder.typicode.com/posts/1")

# 4. Add the fetched data to memory as the assistant's response
if fetched_data is not None:
    scout.add_to_memory("assistant", str(fetched_data))

# 5. Save the state to the hard drive
scout.save_agent_state()