from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from createbot import dp
from data_base import databot_db

class FSMFindPeople(StatesGroup):
    FindPeopleName = State()

# @dp.message_handler(commands=['find_people'], state=None)
async def find_people(msg: types.Message):
    await FSMFindPeople.FindPeopleName.set()
    await msg.reply(f'Введите ФИО человека в формате "Фамилия Имя Отчетсво"')

# @dp.message_handler(content_types=['text'], state=FSMFindPeople.FindPeopleName)
async def Load_Find_People_Name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['FindPeopleName'] = msg.text
        databot_db.cur.execute("SELECT * FROM `phonebook` WHERE `name` = ?", (data['FindPeopleName'],))
        FindPeople = databot_db.cur.fetchone()
        await msg.answer(f'<b>Вот человек, которого Вы искали:</b>\n{FindPeople[0]} {FindPeople[1]} {FindPeople[2]} {FindPeople[-1]}')
        await state.finish()

def register_handlers_find_people(dp: Dispatcher):
    dp.register_message_handler(find_people, commands=['find_people'], state=None)
    dp.register_message_handler(Load_Find_People_Name, content_types=['text'], state=FSMFindPeople.FindPeopleName)