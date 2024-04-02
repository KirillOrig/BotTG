import sqlite3 as sq
from aiogram import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

async def on_startup(_):
    print('Бот вышел в онлайн')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

with sq.connect("databot.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS peoples (
        name TEXT,
        number TEXT,
        date_of_birth TEXT,
        mail TEXT)""")

class FSMData(StatesGroup):
    FullName = State()
    Number = State()
    DateOfBirth = State()
    Mail = State()

# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute("INSERT INTO peoples VALUES (?, ?, ?, ?)", tuple(data.values()))
#         cur.commit()

button_help = KeyboardButton("/help")
button_list = KeyboardButton("/show_list")
button_add_people = KeyboardButton("/add_people")
button_dell_people = KeyboardButton("/dell_people")

kb_but = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_but.row(button_help, button_list).row(button_add_people, button_dell_people)
