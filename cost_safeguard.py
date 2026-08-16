try:
    requests = int(input("Enter the number of API requests you plan to make: "))
    words = int(input("Enter the average number of words per request: "))
except ValueError:
    print("ERROR: Invalid input. Please enter numbers only.")
    exit()

# Core Math
total_words = requests * words
total_tokens = total_words * 1.3
total_cost = (total_tokens / 1000) * 0.002  # Updated to $0.002 per 1k tokens

# Logic Gates with Currency Formatting (:.2f)
if total_cost <= 5.00:
    print(f"Status: Approved! Total cost: ${total_cost:.2f}")
elif total_cost <= 50.00:
    print(f"Status: Warning. Manager approval required. Total cost: ${total_cost:.2f}")
else:
    print(f"Status: BLOCKED! Exceeds budget limit. Total cost: ${total_cost:.2f}")