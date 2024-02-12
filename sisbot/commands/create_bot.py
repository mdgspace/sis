import os
import argparse
from . import codes
import sys

def create_bot(bot_name):
    # Get the parent directory of the current directory (parallel to sisbot)
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    
    # Create the bot directory parallel to sisbot
    bot_dir = os.path.join(parent_dir, bot_name)
    os.makedirs(bot_dir, exist_ok=True)

    # Change current working directory to the newly created bot directory
    os.chdir(bot_dir)
    scripts = os.makedirs("scripts")
    services = os.makedirs("services")

    
    patterns_file = os.path.join(bot_dir, 'patterns.py')
    views_file = os.path.join(bot_dir, 'views.py')

    with open(patterns_file, 'w') as f:
        f.write(codes.patterns_code)
    with open(views_file, 'w') as f:
        pass

    services_dir = os.path.join(bot_dir, 'services')
    
    for filename, content in codes.service_files.items():
        file_path = os.path.join(services_dir, filename)
        with open(file_path, 'w') as f:
            f.write(content)

    print(f"Bot '{bot_name}' created successfully.")


def run():

    parser = argparse.ArgumentParser(description="Manage the project")
    subparsers = parser.add_subparsers(dest="command")

    # create_bot command
    create_bot_parser = subparsers.add_parser("create_bot", help="Create a new bot")
    create_bot_parser.add_argument("bot_name", help="Name of the bot directory to create")

    args = parser.parse_args()

    if args.command == "create_bot":
        create_bot(args.bot_name)
    else:
        print("Command not recognized.")


if __name__ == "__main__":
    run()