from aiogram import executor
from createbot import dp
from data_base import databot_db

async def on_startup(_):
    print('Бот вышел в онлайн')
    databot_db.sql_start()

from handlers import users, editdata, dellpeople, delldata, addpeople

users.register_handlers_users(dp)
addpeople.register_handlers_addpeople(dp)
dellpeople.register_handlers_dellpeople(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
