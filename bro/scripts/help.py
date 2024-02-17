def help(message):
    helpTxt = f'here are all the commands:\n' 'bro @<user> has <key_name> : assigns key to an user\n' 'bro info keys / bro who has keys : current possessions of keys\n' 'bro scores : display everone\' score\nbro score <year> : scores of a year\n' 'bro ping : bro pong\n' 'bro who is @<user> : roles of the given user\nbro <@user> is <role> : assigns a role to an user\n' 'bro birthday @<user> : Gives the DOB of given user' 
        
    
    return helpTxt    
    
    

# (r"bro <@(.{11})> has (\w+)" , views.bro_keys_claim),
# (r"^bro info keys$", views.bro_keys),
# (r"^bro who has keys$", views.bro_keys),

# (r"^bro scores$", views.bro_score_message),
# (r"<@(.{11})> \+\+|<@(.{11})>\+\+|<@(.{11})>--|<@(.{11})> --" , views.handle_user_score),

# (r"bro ping", views.bro_ping),
# (r"bro test test1", views.testing_message),

# (r"(good night|goodnight|cya|bye|nighty night)", views.bye),

# (r"bro who is <@(.{11})>", views.getRole),
# (r'bro <@(.{11})> is (\w+)', views.setRole),
# # (r'bro <@(.{11})> is (\w+)', views.setRole)

# (r"bro score (\w+)$", views.batchScore),

# (r"bro birthday <@(.{11})>", views.birthday)