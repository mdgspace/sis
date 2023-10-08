import os


def init():
    pass


def load_apps():
    apps = os.environ.get("APPS")


def resolve_message(message: str):
    bot = message.split()[0]
    if bot == "sis":
        return "sisbot"
    elif bot == "bro":
        return "bro"
    else:
        return None
