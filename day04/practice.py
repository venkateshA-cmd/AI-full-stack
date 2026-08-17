import requests

url = "https://jsonplaceholder.typicode.com/users"


try:
    response = requests.get(url,timeout=5)

    if response.status_code == 200:

        data  = response.json()
        for data in data:

            print(f"Data Retrived for:{data["name"],data["email"]}")
        
    else:
        print(f"Error:Server responded with status {response.status_code}")
    

except requests.exceptions.RequestException as e:
    print(f"Network failure:{e}")

