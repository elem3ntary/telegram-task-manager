from telebot import TeleBot
from telebot.types import Message
from .config import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["add"])
def add(message: Message):
