from . import services
from ...services import dB

def handle_user_info(message):
    user = services.extract_user(message)
    user_data = dB.load_user_data()
    print(user)
    user_info = user_data[user]
    print(user_info)
    result = ""
    for key, value in user_info.items():
        print(f"{key} : {value},\n")
        result += f"{key} : {value},\n"
    
    return result