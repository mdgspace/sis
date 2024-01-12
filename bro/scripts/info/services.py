import re


def extract_user(message):
    pattern = '<@(.{11})>'
    list = message.split()
    test_user = list[2]
    match = re.search(pattern , test_user)
    user = match.group(1)
    
    return user

