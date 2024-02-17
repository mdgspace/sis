from ...services import redisService

redisStore = redisService.RedSis()
redisStore.redisInit()

utilDict = {
    "1y" : "1st",
    "2y" : "2nd",
    "3y" : "3rd",
    "4y" : "4th"
}


def getBatchScore(message, batch):
    batch = utilDict[batch]
    userDB = redisStore.getValue('userDBtest1')
    batches = redisStore.getValue('batchesData')
    msg = ''   
    print(batch)
    if(batches.get(batch, False)):
        print("------")
        users = batches[batch]
        for user in users:
            print(user)
            score = userDB[user]["score"]
            msg += f'<@{user}> : {score}\n'
        return msg
    return f'No score info yet X_x'
    
        
        
    
