import sys
from sisbot.commands import create_bot
def main():
    if len(sys.argv) != 3 or sys.argv[1] != 'create_bot':
        bot_name = sys.argv[2]
        print("Usage: python manage.py create_bot <bot_name>")
        sys.exit(1)

   
    create_bot.run()

if __name__ == "__main__":
    main()
