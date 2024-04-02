from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from createbot import dp
from data_base import databot_db

class FSMDellName(StatesGroup):
    DellName = State()

# @dp.message_handler(commands=['dell_people'], state=None)
async def dell_people(msg: types.Message):
    await FSMDellName.DellName.set()
    await msg.reply(f'Введите ФИО человека в формате "Фамилия Имя Отчетсво"')

# @dp.message_handler(content_types=['text'], state=FSMDellName.DellName)
async def Load_Dell_Name(msg: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['DellName'] = msg.text
            databot_db.cur.execute("SELECT * FROM `phonebook` WHERE `name` = ?", (data['DellName'],))
            people = databot_db.cur.fetchone()
            if people:
                databot_db.cur.execute('DELETE FROM `phonebook` WHERE `name` = ?', (data['DellName'],))
                databot_db.base.commit()
                await msg.answer('Человек успешно удален')
            else:
                await msg.answer('Данного человека нет в базе данных')
            await state.finish()
    except Exception as a:
        await msg.answer(f'Ошибка: {a}')

def register_handlers_dellpeople(dp: Dispatcher):
    dp.register_message_handler(dell_people, commands=['dell_people'], state=None)
    dp.register_message_handler(Load_Dell_Name, content_types=['text'], state=FSMDellName.DellName)