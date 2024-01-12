import os
 
API_KEY = os.environ.get("GOOGLE_API_KEY")

def handle_google_map_query(message):
    parts = message.split()
    if len(parts) > 3 and parts[0] == "bro" and parts[1] == "map" and parts[2] == "me":
            query = " ".join(parts[3:])
            print(f"Query: {query}")
    else:
            print("Invalid format")
    
    map_zoom = '14'
    map_size = '600x400'
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={query}&zoom={map_zoom}&size={map_size}&key={API_KEY}"

    print(map_url)
    return map_url