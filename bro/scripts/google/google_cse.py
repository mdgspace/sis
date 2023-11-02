
import requests
import os
import re

API_KEY = os.environ.get("GOOGLE_API_KEY")
CX = os.environ.get("GOOGLE_CSE_ID")
print(API_KEY , CX)
      
def handle_google_image_query(message):
    parts = message.split()
    if len(parts) > 3 and parts[0] == "bro" and parts[1] == "image" and parts[2] == "me":
        query = " ".join(parts[3:])
        print(f"Query: {query}")
    else:
        print("Invalid format")

    
    try:
        response =  requests.get(f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}&searchType=image")
        data = response.json()
        print(data["items"][0]["link"])
        if "items" in data and len(data["items"]) > 0:
            return data["items"][0]["link"]
        else:
            return None
    
    except Exception as e:
        print(e)
        return None
        

def handle_google_animate_query(message):
    parts = message.split()
    if len(parts) > 3 and parts[0] == "bro" and parts[1] == "animate" and parts[2] == "me":
        query = " ".join(parts[3:])
        print(f"Query: {query}")
    else:
        print("Invalid format")

    
    try:
        response =  requests.get(f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}&searchType=image&fileType=gif")
        data = response.json()
        print(data["items"][0]["link"])
        if "items" in data and len(data["items"]) > 0:
            return data["items"][0]["link"]
        else:
            return None
    
    except Exception as e:
        print(e)
        return None

    





#async def handle_google_animate_query(message):
