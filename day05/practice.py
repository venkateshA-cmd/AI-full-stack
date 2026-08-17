class LLMClient:

    def __init__(self,api_key,model_name):
        self.key = api_key
        self.model = model_name
        self.request_count = 0

    def make_request(self,prompt):
        self.request_count += 1
        print(f"[{self.model}] sending prompt:{prompt}")
        print(f"Total requests made my this client:{self.request_count}")

agent1 = LLMClient(api_key="sh-123",model_name="GPT-4o")
agent2 = LLMClient(api_key="sk-123",model_name="Claude-3.5")

agent1.make_request("Hello GPT!")
agent1.make_request("Translate this.")
agent2.make_request("Hello Claude!")


class DatabaseConnection:

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.is_connected = True

    def connect(self):
        self.is_connected = True
        print(f"{self.host}Connecting...to{self.port} with status[{self.is_connected}]")

connect1 = DatabaseConnection(host="180.92.010.20",port = "5050")
connect2 = DatabaseConnection(host="200.220.150.230",port="8050")

connect1.connect()
connect2.connect()
        