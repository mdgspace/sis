from . import views

patterns = [
    
    (r"bro <@(.{11})> has (\w+)" , views.bro_keys_claim),
    (r"^bro info keys$", views.bro_keys),
    (r"^bro who has keys$", views.bro_keys),
    
    (r"^bro scores$", views.bro_score_message),
    (r"<@(.{11})> \+\+|<@(.{11})>\+\+|<@(.{11})>--|<@(.{11})> --" , views.handle_user_score),
    (r"bro ping", views.bro_ping),
    (r"bro test test1", views.testing_message)

    
]