from ...services import redisService
from . import schema


#Initializing Refis Client

redis_client = redisService.RedSis()
redis_client.redisInit()


# Function to load key ownership data from a YAML file
def load_keys_data():
    keys_data = redis_client.getValue("keys_data")

    if keys_data is None:
        keys_data = {"keys": {}}
    
    return keys_data


# Function to save key ownership data to a YAML file
def save_keys_data(keys_data):    
    redis_client.setValue("keys_data", keys_data)




# Function to extract user ID and key name from a message
def extract_user_and_key(message):
    parts = message.split()
    user_id = parts[1]
    key_name = parts[3]
    return user_id.strip(), key_name.strip()
