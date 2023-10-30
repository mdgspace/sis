import os
from slack_bolt import App
from ...services import dB
from . import services
# Function to initialize user scores data from a YAML file

def handle_user_score(message):
 
    user, operator = services.extract_user_and_operator(message)
    print(f"{user} , {operator}")

    user_data = dB.load_user_data()
    user_info = user_data[user]
    print(user_data)

    if user and operator and user_info:
        if(operator == '++'):
            user_info["score"] = str( int(user_info['score']) + 1)
            compliment = compliment = "Great job! "
        elif(operator == '--'):
            user_info['score'] = str( int(user_info['score']) - 1)
            compliment = "Oops! Your score decreased by 1."
        
    else:
        return f"<@{user}>??? who the fuck are  you"        

        # Save the updated data to the YAML file
    dB.save_user_data(user_data)
    print(user_data)

    return f"<@{user}>\'s score is now {user_info['score']}.{compliment}"


def handle_bro_scores_message(message):
    
    user_data = dB.load_user_data()
    user_scores_message = "User Scores:\n"
    for user, data in user_data.items():
        if(data['Year'] != 'Alumni'):
            user_scores_message += f"<@{user}>: {data['score']}\n"

    return user_scores_message
   



    '''blocks = [
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
    
    return view_data'''
