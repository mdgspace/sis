from ...services import redisService

redisStore = redisService.RedSis()
redisStore.redisInit()

def getBirthday(userId):
    userDB = redisStore.getValue('userDBtest1')
    if(userDB.get(userId, False)):
        if(userDB[userId].get('dob', False)):
            dob = userDB[userId]['dob']
            return f'Wish <@{userId}> on {dob}!'
        
    return f'<@{userId}> who? Can\' recognise them :/'