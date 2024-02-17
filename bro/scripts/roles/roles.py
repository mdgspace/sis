from ...services import redisService



redisStore = redisService.RedSis()
redisStore.redisInit()

def handleDeleteRole(userId, notRole):
    userDB = redisStore.getValue('userDBtest1')
    if(userDB.get(userId, False)):
        userRoles = userDB[userId]['roles']
        if(notRole.lower() in userRoles):
            userRoles.remove(notRole.lower())
            userDB[userId]['roles'] = userRoles
            redisStore.setValue('userDBtest1', userDB)
            return f'<@{userId}> is no longer {notRole}'
        role = 'not '+ notRole
        userRoles.append(role.lower())
        userDB[userId]['roles'] = userRoles
        redisStore.setValue('userDBtest1', userDB)
        return f'OK! <@{userId}> is {role}' 
        
        
    
    

def handleSetRole(userId, role):
    userDB = redisStore.getValue('userDBtest1')
    if(userDB.get(userId, False)):
        userRoles = userDB[userId]['roles']
        if(role.lower() in userRoles):
            return f'<@{userId}> is already {role}'
        userRoles.append(role.lower())
        userDB[userId]['roles'] = userRoles
        redisStore.setValue('userDBtest1', userDB)
        # print(userDB[userId]['roles'])
        # print(redisStore.getValue('userDBtest1')[userId]['roles'])
        return f'OK! <@{userId}> is {role}' 
    else:
        return f'<@{userId}> ?? never heard of them :(' 
        
    

def handleGetRole(userId):
    userDB = redisStore.getValue('userDBtest1')
    userEntity = userDB[userId]
    userRoles = userEntity['roles']
    print(userRoles)
    
    roleScript = ''
    
    for role in userRoles:
        roleScript += role + ', '
        
    roleScript = roleScript[:-2] + '.'
    
    return f'<@{userId}> is {roleScript}'

