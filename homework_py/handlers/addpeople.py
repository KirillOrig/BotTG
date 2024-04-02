from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

@dp.message_handler(commands=['add_people'], state=None)
async def add_people(msg: types.Message, state: FSMContext):
    await FSMData.FullName.set()
    await msg.reply(f'Введите ФИО человека в формате "Фамилия Имя Отчетсво"')

@dp.message_handler(content_types=['FullName'], state=FSMData.FullName)
async def Load_Full_Name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['FullName'] = msg.text
    await FSMData.next()
    await msg.reply(f'Введите номер телефона человека')

@dp.message_handler(state=FSMData.Number)
async def Load_Number(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Number'] = msg.text
    await FSMData.next()
    await msg.reply(f'Введите дату рождения в формате "xx.xx.xxxх"')

@dp.message_handler(state=FSMData.DateOfBirth)
async def Load_Number(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['DateOfBirth'] = msg.text
    await FSMData.next()
    await msg.reply(f'Введите электронную почту человека')

@dp.message_handler(state=FSMData.Mail)
async def Load_Number(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Mail'] = msg.text

    # await sql_add_command(state)
    await state.finish()