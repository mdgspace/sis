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
      self.r.set('key', 'value')
    except Exception as e:
      print(f"[REDIS] error in setting the value [{key}] : {str(e)}")
  
  
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

def main():
  lol = RedSis()
  lol.redisInit()
  lol.setValue('hell', 'hi')
  print(lol.getValue('hell'))
  lol.setValue('hell', 'new')
  print(lol.getValue('hell'))


if __name__ == "__main__":
    main()
'''
redis_client = RedSis()
redis_client.redisInit()
lab_status = {
   "status" : "open",
}
redis_client.setValue("test_lab_status" , lab_status)
status = redis_client.getValue("test_lab_status")
print(status)'''

                       


if __name__ == "__main__":
   pass


"""
def process_csv_and_store_data():
    individuals = {}
    
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            
            

            individual_data = {
                "Name": row['Name'],
                "Phone No": row['Phone No'],
                "Email Id": row["Email Id"],
                "DOB": row['DOB'],
                "Year": row['Year'],
                "Branch": row['Branch'],
                "Enrollment Number": row['Enrollment Number'],
                "Room No": row['Room No'],
                "GITHUB ID": row['GITHUB ID'],
                "FB ID": row['FB ID'],
                "SLACK USER ID": row['SLACK USER ID'],
                "membership_status": row["membership_status"],
                "Home Address": row['Home Address'],
            }
            
            individuals[individual_data['Email Id']] = individual_data


    
    redis_client.setValue('all_individuals', individuals)

    #data = redis_client.getValue('all_individuals')
    test = redis_client.getValue('all_individuals')
    data = test['agarwalpratham1812@gmail.com']
    data1 = data['Name']
    return data1


all_data = process_csv_and_store_data()

print(all_data)"""





  

