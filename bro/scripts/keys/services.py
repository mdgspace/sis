import yaml
from ...services import redisService
from . import schema


#Initializing Refis Client

redis_client = redisService.RedSis()


# Function to load key ownership data from a YAML file
def load_keys_data():
    keys_data = redis_client.get_data("keys_data")

    if keys_data is None:
        keys_data = {"keys": {}}

    validate_data(keys_data, schema.keys_data_schema)
    
    return keys_data


# Function to save key ownership data to a YAML file
def save_keys_data(keys_data):
    validate_data(keys_data, schema.keys_data_schema)
    
    redis_client.set_data("keys_data", keys_data)



#Validation of Schema
def validate_data(data, schema):
    for field, field_info in schema.items():
        if field in data:
            field_type = field_info.get("type")
            field_nullable = field_info.get("nullable", True)
            
            if not isinstance(data[field], field_type):
                raise ValueError(f"Field '{field}' is of the wrong type.")
            if not data[field] and not field_nullable:
                raise ValueError(f"Field '{field}' cannot be null.")
        else:
            if not field_nullable:
                raise ValueError(f"Field '{field}' is missing.")



# Function to extract user ID and key name from a message
def extract_user_and_key(message):
    parts = message.split(" has ")
    if len(parts) == 2:
        sub_parts = parts[0].split()
        user_id = sub_parts[1]
        key_name =  parts[1]
        return user_id.strip(), key_name.strip()
    return None, None