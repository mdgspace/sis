from ...services import redisService
import re
from .schema import scores_data_schema


redis_client = redisService.RedSis()
redis_client.redisInit()


def extract_user_and_operator(message):
    pattern = '<@(.{11})>(\+\+)|<@(.{11})>.(\+\+)|<@(.{11})>(\-\-)|<@(.{11})>.(\-\-)'
    lister = re.findall(pattern , message)
    user = lister[0][0] or lister[0][2] or lister[0][4] or lister[0][6]
    operator = lister[0][1] or lister[0][3] or lister[0][5] or lister[0][7]

    # print(lister)
    # print(user)
    
    
    
    return user , operator
