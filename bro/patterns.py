from . import views

patterns = [
    (r"^yo\s", views.yo),
    (r"^bro\s", views.bro),
    (r"bro <@([A-Z0-9]+)> has ([A-Z0-9]+)" , views.bro_keys_claim)
    (r"^bro info keys$", views.bro_keys),
    (r"^bro who has keys$", views.bro_keys)
    (r"^bro scores$", views.handle_bro_scores_message)
    (r"<@([A-Z0-9]+)> \+\+|<@([A-Z0-9]+)> --" , views.handle_user_score)

    
]