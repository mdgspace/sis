import os
import re
from importlib import import_module


allowed_patterns = []


def init():
    load_apps()


def load_apps():
    apps = [
        "sis" , 
        "bro"
            ]
    # apps = ["bro", "sis"]
    for app in apps:
        mod = import_module(f"{app}.patterns")
        for pattern in mod.patterns:
            allowed_patterns.append(pattern)


def route(message: str):
    response = ""
    for pattern in allowed_patterns:
        if re.match(pattern[0], message):
            print(f"Matched {pattern[0]}")
            # Not returning here so that allpatterns are matched
            response = pattern[1]()
    return response


if __name__ == "__main__":
    load_apps()




