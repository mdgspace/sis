from . import services
from . import services


        
def handle_key_claim(message):
    keys_data = services.load_keys_data()

    user_id, key_name = services.extract_user_and_key(message)

    if user_id and key_name:
        keys_data["keys"][key_name] = {"owner": user_id}

        services.save_keys_data(keys_data)

        return f"<{user_id}> now has {key_name}."
    


def handle_bro_keys_message():
    keys_data = services.load_keys_data()

    result = ""

    for key, data in keys_data.get("keys", {}).items():
        owner = data.get("owner")
        result += f"*{key}* : {owner}\n"

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
    

