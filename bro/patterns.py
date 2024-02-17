from . import views

patterns = [
    (r"bro <@(.{11})> has (\w+)" , views.bro_keys_claim),
    (r"^bro info keys$", views.bro_keys),
    (r"^bro who has keys$", views.bro_keys),
    (r"bro info <@(.{11})>" , views.user_info),
    (r"^bro scores$", views.bro_score_message),
    
    
    
    
    (r"<@(.{11})> \+\+|<@(.{11})>\+\+|<@(.{11})>--|<@(.{11})> --" , views.handle_user_score),
    (r"bro score (\w+)$", views.batchScore),
    
    (r"bro ping", views.bro_ping),
    (r"bro test test1", views.testing_message),
    
    (r"(good night|goodnight|cya|bye|nighty night)", views.bye),
    
    (r"bro who is <@(.{11})>", views.getRole),
    (r'bro <@(.{11})> is (\w+)', views.setRole),
    # (r'bro <@(.{11})> is (\w+)', views.setRole)
    
    (r"bro birthday <@(.{11})>", views.birthday),
    (r'bro help', views.help)
    
    
    
    (r"<@(\w+)>\s*(\+\+|\-\-)" , views.bro_user_scores),
    (r"bro animate me (.+)" , views.google_animate_query),
    (r"bro image me (.+)" , views.google_image_query),
    (r"bro map me (.+)" , views.google_map_query),
    (r"bro quote (.+)|bro quote" , views.bro_quote),
    (r"bro toss" , views.bro_toss) ,
    (r"bro dice" , views.bro_dice),
    (r".*lab is (open|closed)*" , views.bro_lab_status),
    (r".*is lab (open|closed)*" , views.bro_isLab_status)
]
