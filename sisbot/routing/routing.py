import os
import re
from sis import patterns

allowed_patterns = []


def init():
    pass


def load_apps():
    apps = os.environ.get("APPS")
    
def route(message: str):
    print("Routing")
    for pattern in patterns.patterns:
        if re.match(pattern[0], message):
            # print(f"Matched {pattern[0]}")
            return pattern[1]()
        

if __name__ == "__main__":
    route("bro help")
