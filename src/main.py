from dotenv import load_dotenv
import logging
from models.bot import Bot

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    filename="discord.log",
    encoding="utf-8",
    filemode="w"
)

bot = Bot()
bot.run(bot._token)