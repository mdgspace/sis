from . import services
import yaml
# Function to manage key ownership data
def handle_key_claim(message):
    # Initialize key ownership data from a YAML file
    filename = "keys_data.yaml"
    keys_data = services.load_keys_data(filename)

    user_id, key_name = services.extract_user_and_key(message)

    if user_id and key_name:
            # Update the owner of the key in the data dictionary
        for key_info in keys_data.get("keys", []):
            if key_info["name"] == key_name:
                key_info["owner"] = user_id
                break

            # Save the updated data to the YAML file
            services.save_keys_data(keys_data, filename)

            return f"<{user_id}> now has {key_name}."

   
def handle_bro_keys_message():
     
    with open('keys_data.yaml', "r") as file:
            keys_data = yaml.safe_load(file)
            print(keys_data)
   
     

    # Generate a table of key ownership using Slack Bolt blocks
        

    for key_info in keys_data.get("keys", []):
        key = key_info["name"]
        owner = key_info["owner"] if key_info["owner"] else "null"
        return f"*{key}* : {owner} \n"

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
    

