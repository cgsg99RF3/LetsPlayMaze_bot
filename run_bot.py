from src.bot_interface import BotInterface


if __name__ == '__main__':
    bot_token = '7147524292:AAHZmhqTSvQTnVBw4P5poxRbOxZw5kvGs38'
    bot = BotInterface(bot_token)
    bot.run()