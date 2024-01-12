from  ...services import dB
import re
from ...services import redisService

redis_client = redisService.RedSis()
redis_client.redisInit()


def handle_lab_status(message):
    pattern = r"\blab is (open|closed)\b"
    match = re.search(pattern, message)
    test = match.group()
    #print(test)
    txt = test.split()
    text = txt[2]
    #print(text)

    lab_status = dB.laod_lab_status()
    print(lab_status)
    response = ""
    if text == 'open':
        if(lab_status['status'] == 'open'):
           response = f"hahaha lab is already {lab_status['status']}"
        else:
            lab_status['status'] = 'open'
            response = f"Okay, Lab is {lab_status['status']}"
    elif text == 'closed':
        if(lab_status['status'] == 'closed'):
           response = f"hahaha lab is already {lab_status['status']}"
        else:
            lab_status['status'] = 'closed'
            response = f"Okay, Lab is {lab_status['status']}"
    
    dB.save_lab_status(lab_status)    
    print(lab_status)
    return response



def handle_isLab_status(message):
    print('hi')
    pattern = r"\bis lab (open|closed)\b"
    match = re.search(pattern, message)
    test = match.group()
    print(test)
    #print(test)
    txt = test.split()
    text = txt[2]
    print(text)

    response = ""
    lab_status = dB.laod_lab_status()

    if text == 'open':
        if(lab_status['status'] == 'open'):
           response = f"Yes, the lab is open"
        else:
            response = f"No, the lab is closed"
    elif text == 'closed':
        if(lab_status['status'] == 'closed'):
           response = f"Yes, the lab is closed"
        else:
            lab_status['status'] = 'closed'
            response = f"No, the Lab is open"

    return response