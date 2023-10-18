import os
import yaml
from slack_bolt import App
from . import services

# Function to initialize user scores data from a YAML file

def handle_user_score(message):
    filename = "user_scores.yaml"
    user_scores_data = services.initialize_user_scores_from_file(filename)
    user, operator = services.extract_user_and_operator(message)

    if user and operator:
        # Find the user in the data dictionary
        for user_info in user_scores_data.get("users", []):
            if user_info["name"] == user:
                if operator == "++":
                    user_info["score"] += 1
                    compliment = "Great job! Your score increased by 1."
                else:
                    user_info["score"] -= 1
                    compliment = "Oops! Your score decreased by 1."
                break

        # Save the updated data to the YAML file
        services.save_user_scores_to_file(user_scores_data, filename)

        return f"{user}\'s score is now {user_info['score']}. {compliment}"


def handle_bro_scores_message():
    filename = "user_scores.yaml"
    user_scores_data = services.initialize_user_scores_from_file(filename)
    
    blocks = [
        {
            "type": "section",
            "block_id": "user_scores",
            "text": {
                "type": "mrkdwn",
                "text": "SCORECARD"
            }
        },
        {
            "type": "divider"
        }
    ]

    # Add user scores information to the blocks
    for user_info in user_scores_data.get("users", []):
        name = user_info["name"]
        score = user_info["score"]
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{name} - {score}*"
                }
            }
        )

    # Create a view with the blocks
    view_data = {
        "type": "modal",
        "callback_id": "user_scores_modal",
        "title": {
            "type": "plain_text",
            "text": "User Scores"
        },
        "blocks": blocks
    }
    
    return view_data
