import schedule
import time
import datetime

def your_function():
    print("Your function is running at exactly .")

# Schedule the function to run at 00:05 AM every day
schedule.every().day.at("17:41").do(your_function)
    
def broCron():
    schedule.run_pending()
    print('chck')
