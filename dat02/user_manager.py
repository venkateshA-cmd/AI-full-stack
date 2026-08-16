import json

def save_database():
    with open("users_db.json","w") as file:
        json.dump(users_db,file,indent=4)

def load_database():
    try:
        with open("users_db.json","r") as file:
           loaded_database = json.load(file)
           return loaded_database
    except FileNotFoundError:
        print("users_db json is not exist!...")
        return {}

    
users_db = load_database()

def add_user():
    username = input("Enter your name:")
    if username in users_db:
        print("Error: User already exists.")
    else:
        users_db[username] = {"limit":100,"history":[]}
        print("User added successfully.")
    save_database()


def log_activity():
    username = input("Enter your name:")
    if username not in users_db:
        print("Error: User Not Found")
    else:
        action = input("Choose your action:")
        users_db[username]["history"].append(action)
        
        # Decrement by 10 (cleaner syntax)
        users_db[username]["limit"] -= 10
        
        # The missing business logic:
        if users_db[username]["limit"] <= 0:
            print("WARNING: User is out of API credits!")
        else:
            print(f"Action logged. Remaining credits: {users_db[username]['limit']}")
        save_database()

def view_database():
     print(users_db)

# The Main Server Loop
while True:
    print("\n--- SERVER MENU ---")
    print("1. Add User")
    print("2. Log Activity")
    print("3. View DB")
    print("4. Shut Down Server")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        add_user()
    elif choice == "2":
        log_activity()
    elif choice == "3":
        view_database()
    elif choice == "4":
        print("Shutting down server...")
        break # This stops the infinite loop
    else:
        print("Invalid choice. Try again.")



        
    

    
