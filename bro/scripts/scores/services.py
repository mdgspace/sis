from ...services import redisService
import re
from .schema import scores_data_schema
redis_client = redisService


def load_user_scores_data():
    user_scores_data = redis_client.get_data("user_scores_data")

    if user_scores_data is None:
        user_scores_data = {"users": {}}

    validate_data(user_scores_data,scores_data_schema)
    
    return user_scores_data

# Function to save user scores data to Redis
def save_user_scores_data(user_scores_data):
    validate_data(user_scores_data, scores_data_schema)
    
    redis_client.set_data("user_scores_data", user_scores_data)

# Validate data against a schema
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


def extract_user_and_operator(text):
    pattern = r"@([A-Z0-9]+) (\+\+|--)"
    
    match = re.search(pattern, text)

    if match:
        user = f"@{match.group(1)}"
        operator = match.group(2)  
        return user, operator
    else:
        return None  # No match found