from aiogram import Bot, Dispatcher
import os

TOKEN = "6838128532:AAGiEAvJTIxx_kakgqRyRBM8o2-ljWBYptc"
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)