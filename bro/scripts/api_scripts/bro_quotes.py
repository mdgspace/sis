import requests
import os


API_KEY = os.environ.get('NINJAS_API_KEY')
print(API_KEY)

def handle_quote(message):
    parts = message.split()
    if parts[0] == "bro" and parts[1] == "quote":
        category = " ".join(parts[2:])
        print(f"Query: {category}")
    else:
        category = ""
    
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
        print(response.text)
        data = response.json()
        print(data)
        return data[0]['quote']
    else:
        print("Error:", response.status_code, response.text)

    
