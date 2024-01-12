from . import redisService

redis_client = redisService.RedSis()
redis_client.redisInit()

def load_user_data():
    
    user_data = redis_client.getValue("userDBtest1")

    if user_data is None:
        user_data = None

    
    return user_data

# Function to save user scores data to Redis
def save_user_data(user_data):
    
    redis_client.setValue("userDBtest1", user_data)

def laod_lab_status():
    lab_status = redis_client.getValue("test_lab_status")

    if lab_status is None:
        lab_status = None
    
    return lab_status


def save_lab_status(lab_status):
    redis_client.setValue("test_lab_status" , lab_status)