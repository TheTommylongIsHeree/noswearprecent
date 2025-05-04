from src import Bot
import discord

def main():
    from os import getenv
    from dotenv import load_dotenv
    load_dotenv()
    
    bot = Bot()
    bot.run(getenv("TOKEN"))

if __name__ == "__main__":
    main()
