import redis
import os
from dotenv import load_dotenv
import json
import csv

load_dotenv()

class RedSis:
  r=0
  
  def redisInit(self):
    try:
      self.r = redis.Redis(
        host=os.environ.get("REDIS_HOST"),
        port=os.environ.get("REDIS_PORT"),
        password=os.environ.get("REDIS_PASSWORD")
      )
      #could be better connections depending on the bot using the store
      # print("[REDIS] Connection successful")
    except:
      print("[REDIS] Connection Failed")
    
  def setValue(self, key:str, value):
    try:
      if(isinstance(value,dict)):
        value_json = json.dumps(value)
        self.r.set(key, value_json)
        return

      self.r.set(key, value)
    except:
      print(f"[REDIS] error in setting the value [{key}]")
  
  def getValue(self, key):
    try:
            data_json = self.r.get(key)
            if data_json is not None:
                data = json.loads(data_json.decode('utf-8'))
                return data
            else:
                return None
    except Exception as e:
            print(f"Error in getting data: {str(e)}")
            return None
    



# # lol.setValue("keys_data", keys_data)
# print(lol.getValue("keys_data"))


# with open('data.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)

#     for row in csv_reader:
#         member = {
#             "slackMemberId": "",
#             "displayName":"",
        
#             "name": row[0],
        
#             "phoneNo":row[1],
#             "emailId" : row[2],
#             "dob" : row[3],
#             "Year" : row[4],
#             "Branch": row[5],
#             "enrollmentNo" : row[6],
#             "roomNo" : row[7],
#             "githubId": row[8],
#             "fbId": row[9],
#             "homeAddress":row[12],
            
#             "score" : "",
#             "roles" : []
#         }
#         # print(row)
#         members.append(member)
        
    
# userDb = {
#   "members":members
# }




def main():
  # lol.setValue("userDBtest", user_db)
  lol = RedSis()



if __name__ == "__main__":
    main()