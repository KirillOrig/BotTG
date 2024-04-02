import sqlite3 as sq
from createbot import bot
from aiogram import types

def sql_start():
    global base, cur
    base = sq.connect('databot.db')
    cur = base.cursor()
    if base:
        print('База данных успешно была создана или подключена!')
    base.execute("""CREATE TABLE IF NOT EXISTS phonebook (
        name TEXT,
        number TEXT,
        date_of_birth TEXT,
        mail TEXT)""")
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO phonebook VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()