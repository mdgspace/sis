
from scripts.keys.keys import handle_key_claim , handle_bro_keys_message
from scripts.scores.scores import handle_bro_scores_message, handle_user_score



def yo():
    print("bro.views.yo()")
    return "yo"


def bro():
    print("bro.views.bro()")
    return "bro"


def bro_keys_claim(message):
   handle_key_claim(message)

def bro_keys(message): 
    handle_bro_keys_message()

def bro_user_scores(message):
    handle_user_score(message)

def bro_score_message():
    handle_bro_scores_message()

