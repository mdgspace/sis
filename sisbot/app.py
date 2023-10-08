import os
from dotenv import load_dotenv
from slack_bolt import App
from routing.routing import resolve_message

load_dotenv()

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@app.message()
def message_hello(message, say):
    print(message["text"])
    response = resolve_message(message["text"])
    if response != None and response != "":
        say(response)


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
