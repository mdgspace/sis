import yaml

# Function to load key ownership data from a YAML file
def load_keys_data(filename):
    try:
        with open('', "r") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
    
        data = {"keys": []}
    return data

# Function to save key ownership data to a YAML file
def save_keys_data(data, filename):
    with open(filename, "w") as file:
        yaml.dump(data, file)


# Function to extract user ID and key name from a message
def extract_user_and_key(message):
    parts = message.split(" has ")
    if len(parts) == 2:
        sub_parts = parts[0].split()
        user_id = sub_parts[1]
        key_name =  parts[1]
        return user_id.strip(), key_name.strip()
    return None, None