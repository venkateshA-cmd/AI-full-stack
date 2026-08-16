database = {}
database["user_123"] = 50


server_logs = {
    "user_1":["login","download","logout"],
    "user_2":["login"]
}
server_logs["user_2"].append("upload")
print(server_logs["user_2"])

def calculate_tax(amount):
    return amount*0.20

calculate_tax(10000)

while True:
    cmd = input("enter command:")
    if cmd == "exit":
        break
