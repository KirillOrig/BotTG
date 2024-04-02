from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from createbot import dp
from data_base import databot_db

class FSMData(StatesGroup):
    FullName = State()
    Number = State()
    DateOfBirth = State()
    Mail = State()

# @dp.message_handler(commands=['add_people'], state=None)
async def add_people(msg: types.Message):
    await FSMData.FullName.set()
    await msg.reply(f'Введите ФИО человека в формате "Фамилия Имя Отчетсво"')

# @dp.message_handler(content_types=['text'], state=FSMData.FullName)
async def Load_Full_Name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['FullName'] = msg.text
    await FSMData.next()
    await msg.answer(f'Теперь введите номер телефона человека')

# @dp.message_handler(state=FSMData.Number)
async def Load_Number(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Number'] = msg.text
    await FSMData.next()
    await msg.answer(f'Отлично. Введите дату рождения в формате "xx.xx.xxxх"')

# @dp.message_handler(state=FSMData.DateOfBirth)
async def Load_DateOfBirth(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['DateOfBirth'] = msg.text
    await FSMData.next()
    await msg.answer(f'И наконец, введите электронную почту человека')

# @dp.message_handler(state=FSMData.Mail)
async def Load_Mail(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Mail'] = msg.text

    await databot_db.sql_add_command(state)
    await state.finish()

def register_handlers_addpeople(dp: Dispatcher):
    dp.register_message_handler(add_people, commands=['add_people'], state=None)
    dp.register_message_handler(Load_Full_Name, content_types=['text'], state=FSMData.FullName)
    dp.register_message_handler(Load_Number, state=FSMData.Number)
    dp.register_message_handler(Load_DateOfBirth, state=FSMData.DateOfBirth)
    dp.register_message_handler(Load_Mail, state=FSMData.Mail)