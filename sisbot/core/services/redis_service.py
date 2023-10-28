import redis
import os
from dotenv import load_dotenv
import json

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
      print("[REDIS] Connection successful")
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
    

lol = RedSis()
lol.redisInit()

keys_data = {
    "key1": {
        "key_name": "key1",
        "owner": None,
    },
    "key2": {
        "key_name": "key2",
        "owner": None,
    },
    "key3": {
        "key_name": "key3",
        "owner": None,
    },
    "key4": {
        "key_name": "key4",
        "owner": None,
    },
}


# lol.setValue("keys_data", keys_data)
print(lol.getValue("keys_data"))
  

if __name__ == "__main__":
    pass