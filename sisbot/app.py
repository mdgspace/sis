import os
from dotenv import load_dotenv
from slack_bolt import App
from routing.routing import init, route

import csv
from core.services import redis_service


load_dotenv()
os.environ.setdefault('APPS', '.conf.settings.APPS')


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)

# Initialize routing
init()

def populate():
    realNameToSlackId = {}
    userDB = {}
    
    redisStore = redis_service.RedSis()
    redisStore.redisInit()
    
    listed = app.client.users_list()
    memberList = listed["members"]
    
    for member in memberList:
        if(member.get('real_name', False)):
            realNameToSlackId[member["real_name"]] = {
                "id" : member["id"],
                "displayName" : member["profile"]['display_name']
            }
        
    with open('data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            # print(f'{row["Name"]} : if condition: {realNameToSlackId.get(row["Name"], False)}')
            if(realNameToSlackId.get(row["Name"], False)):
                userId = realNameToSlackId[row["Name"]]['id']
                displayName = realNameToSlackId[row["Name"]]['displayName']
                
                userDB[userId] = {
                    "displayName": displayName,
                
                    "name": row["Name"],
                
                    "phoneNo":row['Phone No'],
                    "emailId" : row['Email Id'],
                    "dob" : row["DOB(dd/mm/yyyy)"],
                    "Year" : row['Year'],
                    "Branch": row['Branch'],
                    "enrollmentNo" : row['Enrollment Number'],
                    "roomNo" : row['Room No'],
                    "gitHubId" : row['GITHUB ID'],
                    "slackUserId": row['SLACK USER ID'],
                    
                    "score" : "0",
                    "roles" : []
                }    
                
    ############################## ~~data populated in db
    # redisStore.setValue("userDBtest1",userDB)
    # print(redisStore.getValue("userDBtest1"))
    # redisStore.setValue("nameToUserId",realNameToSlackId)
    # print(redisStore.getValue("nameToUserId"))

# populate()





@app.message()
def message_hello(message, say):
    sender = message['user']
    response = route(message["text"])
    if response != None and response != "":
        say(response)


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
