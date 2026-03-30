
# You will take **any one script** from:
# - Day 01 (System Health Script), or
# - Day 02 (API & JSON Script)

# And enhance it by:
# - Organizing the code into **functions**
# - Adding **basic exception handling** (`try / except`)
# - Improving variable names and readability
# - Ensuring the script does not crash on common errors

import requests
import json

def fetch_user_data(timeout=5, retries=3):
    for attempt in range(retries):
        try:
            nof = int(input("Enter the number of MEowww facts you want: "))

            cat_facts = f'https://meowfacts.herokuapp.com/?count={nof}'

            headers = {
                'Accept': 'application/json'
            }

            response = requests.get(url = cat_facts, headers = headers)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None  # Exit the function if input is invalid
        except requests.RequestException as e:
            print(f"Error fetching API data: {e}")
            if attempt < retries - 1:
                print("Retrying...")
            else:
                print("Max retries reached. Exiting.")
                return None  # Exit the function after max retries

        # Check if the request was successful
        print("Response Code:", response)

        # Parse the JSON response
        return response.json()

# calling the function to fetch data
cat_facts_json = fetch_user_data()

    lst = cat_facts_json['data']

    # Print the cat facts
    for i in range(len(lst)):
        print(f"Fact {i+1}:", lst[i])

















