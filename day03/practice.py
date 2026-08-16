import json

my_data = {"alice":{"limit":100}}

with open("database.json","w") as file:
    json.dump(my_data,file,indent=4)


try:
    with open("database.json","r") as file:
        loaded_data = json.load(file)
        print(loaded_data)
except FileNotFoundError:
    print("No database found,starting fresh.")
    