# sis
A distributable slack app made using Slack Bolt. It is a chat-bot which can handle messages and commands from slack and perform tasks. It is directed at organizations to use this as a utility bot to render tasks from slack itself using messages or slash commands. 

## ENV
We use dotenv package to load our environment variables and thus a `.env` file with following variables nneds to be setup in the root directory:

    SLACK_SIGNING_SECRET=<secret key that slack uses to sign every request>
    SLACK_BOT_TOKEN=<xoxb bot token to subscribe to events>
    SLACK_APP_TOKEN=<xapp app token for setup changes over all installations>
    PORT=optional:<port to be used>

## Setup
Download the github repository or clone it.
```shell script
git clone https://github.com/NanoNish/sis.git
```
Install [poetry](https://python-poetry.org/docs/)

Install all the package dependencies.
```
poetry install
```
Now you can run the app
```shell script
poetry run py ./sisbot/app.py
```
Please use black for formatting
```shell script
poetry run py -m black .
```

## Components
`sisbot` folder is the source folder where all the magic happens
* `app.py`          driver file of the project
* `routing`         message to function/script mapping
* `conf`            all configurations will end up here

`bro | sis` all the subcommands for bro come here
* `patterns.py`     regex patterns and corresponding views
* `views.py`        middleware for parsing message and calling scripts
* `scripts`         all scripts related to bro

## 💬 For commit messages

Please start your commits with these prefixes for better understanding among collaborators, based on the type of commit:

    feat:     (addition of a new feature)
    refactor: (refactoring the code: optimization/ different logic of existing code - output doesn't change, just the way of execution changes)
    docs:     (documenting the code, be it readme, or extra comments)
    fix:      (bug fixing)
    chore:    (chore - beautifying code, indents, spaces, camelcasing, changing variable names to have an appropriate meaning)
    patch:    (patches - small changes in code, mainly UI, for example color of a button, increasing size of tet, etc etc)
    conf:     (configurational settings - changing directory structure, updating gitignore, add libraries, changing manifest etc)
    
Please refer to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) for better commit messages.
