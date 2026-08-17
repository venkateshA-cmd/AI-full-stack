import requests
import json

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            raw_data = response.json() 
            print("✓ Data successfully fetched from server.")
            return raw_data  # WE MUST RETURN THE DATA
        else:
            print(f"Error: Server responded with status {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network failure: {e}")
        return None

def clean_data(raw_data):
    cleaned_dataset = []
    for data in raw_data:
        # We extract only what we need to save memory
        cleaned_dataset.append({
            "post_id": data['id'],
            "title": data['title']
        })
    print(f"✓ Data cleaned. Kept {len(cleaned_dataset)} records.")
    return cleaned_dataset

def save_to_disk(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"✓ Data saved successfully to {filename}")

# ==========================================
# MAIN EXECUTION (The Relay Race)
# ==========================================

# 1. Define the target
target_url = "https://jsonplaceholder.typicode.com/posts"

# 2. Fetch the data and SAVE IT TO A VARIABLE
downloaded_data = fetch_data(target_url)

# 3. Only proceed if the download didn't fail
if downloaded_data is not None:
    # 4. Pass the downloaded data into the cleaner
    processed_data = clean_data(downloaded_data)
    
    # 5. Pass the cleaned data to the disk saver
    save_to_disk(processed_data, "training_data.json")
    print("🚀 Pipeline Complete!")
else:
    print("Pipeline aborted due to network error.")