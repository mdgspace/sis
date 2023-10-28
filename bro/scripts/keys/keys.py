from . import services
from . import services


        
def handle_key_claim(message):
    keys_data = services.load_keys_data()

    user_id, key_name = services.extract_user_and_key(message)
    print(user_id, key_name)

    if user_id and key_name:
        keyNames = ""
        for key , value in keys_data.items():
            keyNames += value["key_name"] + ",\n"
            if(value["key_name"] == key_name):
                value["owner"] = user_id
                services.save_keys_data(keys_data)
                print("yaha tak")
                return f"{user_id} now has {key_name}."
        return f"key name not vallid, here are the valid key:\n{keyNames}"    
        



def handle_bro_keys_message(message):
    keys_data = services.load_keys_data()

    result = ""

    for key, value in keys_data.items():
        key_name = value["key_name"]
        owner = value["owner"]
        result += f"*{key_name}* : {owner}\n"
        
    return result

    













    """blocks = [
        {
        "type": "section",
        "block_id": "key_ownership",
        "text": {
            "type": "mrkdwn",
            "text": "*Key Ownership* :key:"
        }
    },
    {
        "type": "divider"
    }
    ]
    """
        
    """blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{key}*: <@{owner}>"
                }
            }
        )

    # Created a view with blocks
    view_data = {
    "type": "modal",
    "callback_id": "key_ownership_modal",
    "title": {
        "type": "plain_text",
        "text": "Key Handling"
    },
    "blocks": blocks
}

   return view_data
"""
    

