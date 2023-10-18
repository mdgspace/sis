from . import views

patterns = [
    
    (r"bro <@([A-Z0-9]+)> has ([A-Z0-9]+)" , views.bro_keys_claim),
    (r"^bro info keys$", views.bro_keys),
    (r"^bro who has keys$", views.bro_keys),
    (r"^bro scores$", views.bro_score_message),
    (r"<@([A-Z0-9]+)> \+\+|<@([A-Z0-9]+)> --" , views.handle_user_score),

    
]