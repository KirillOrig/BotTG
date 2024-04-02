from aiogram import types, Dispatcher
from createbot import dp, bot
from keyboards import kb_but
from data_base import databot_db

# @dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(f'Привет! Я бот, который запоминает номера и еще некоторые данные человека.', reply_markup=kb_but)

# @dp.message_handler(commands=["help"])
async def help(msg: types.Message):
    await msg.answer(f'<b>Вот список всех моих команд:</b>\n\
/start - начало работы с ботом\n\
/help - показать список команд\n\
/add_people - добавить человека в список\n\
/edit_data - редактировать данные человека\n\
/dell_people - удалить человека из списка\n\
/show_list - показать телефонную книгу\n\
/find_people - найти данные о человеке\n\
')

# @dp.message_handler(commands=["show_list"])
async def show_list(msg: types.Message):
    databot_db.cur.execute('SELECT * FROM `phonebook`')
    fetch = databot_db.cur.fetchall()

    if not fetch:
        await msg.answer(f'У вас нет телефонной книги.')
        return

    ffetch = []
    for number in fetch:
        numbers = f"{number[0]}   {number[1]}   {number[2]}   {number[-1]}\n\n"

        ffetch.append(numbers)

    response = "".join(ffetch)
    await msg.answer(f'<b>Телефонная книга:</b>\n\n' + response, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
    
def register_handlers_users(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(show_list, commands=['show_list'])
    dp.register_message_handler(show_list, commands=['show_list'])