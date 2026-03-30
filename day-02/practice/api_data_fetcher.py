# Create by Devendra Gohare.
# Note for creating virtual environment:
# 1. Open Command Prompt and navigate to your project directory.
# 2. Run the following command to create a virtual environment named venv:
#    pip install virtualenv
#    python -m venv venv

# 3. Activate the virtual environment:
# - On Windows:
#   venv\Scripts\activate.ps1

# - On macOS/Linux:             
#   source venv/bin/activate



import requests
import json

nof = int(input("Enter the number of MEowww facts you want: "))

cat_facts = f'https://meowfacts.herokuapp.com/?count={nof}'

headers = {
    'Accept': 'application/json'
}

response = requests.get(url = cat_facts, headers = headers)

# Check if the request was successful
print("Response Code:", response)

# Parse the JSON response
cat_facts_json = response.json()

lst = cat_facts_json['data']

# Print the cat facts
for i in range(len(lst)):
    print(f"Fact {i+1}:", lst[i])

# Saving cat json data to a file, it will automatically create a file named cat_facts.json in the same directory where this script is located.
with open('cat_facts.json', 'w') as file:
    json.dump(cat_facts_json, file)











