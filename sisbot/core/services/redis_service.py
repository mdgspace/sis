import redis
import os
from dotenv import load_dotenv

load_dotenv()


r = redis.Redis(
  host=os.environ.get("REDIS_HOST"),
  port=os.environ.get("REDIS_PORT"),
  password=os.environ.get("REDIS_PASSWORD")
)

# Redis commands
r.set('hello', 'world')
print(r.get('hello'))

if __name__ == "__main__":
    pass