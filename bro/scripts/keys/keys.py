import os
import yaml
from slack_bolt import App
from slack_bolt.view import view
from slack_bolt.view.blocks import SectionBlock, PlainTextObject, DividerBlock
from slack_bolt.view.composition import MarkdownTextObject
from . import services



# Function to manage key ownership data
def handle_key_claim(message):
    # Initialize key ownership data from a YAML file
    filename = 'keys_data.yaml'
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
    keys_data = services.load_keys_data("keys_data.yaml")

    # Generate a table of key ownership using Slack Bolt blocks
    blocks = [
        SectionBlock(
            text=PlainTextObject(text="Key Ownership", emoji=True),
        ),
        DividerBlock(),
    ]

    for key_info in keys_data.get("keys", []):
        key = key_info["name"]
        owner = key_info["owner"] if key_info["owner"] else "null"
        blocks.append(
            SectionBlock(
                text=MarkdownTextObject(text=f"{key}: <@{owner}>"),
            )
        )

    # Create a view with blocks
    view_data = view(type="modal", blocks=blocks)

    return {
        "text": "Key Ownership:",
        "blocks": view_data
    }

