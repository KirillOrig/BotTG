from aiogram import types, Dispatcher
from createbot import dp
from data_base import databot_db

# @dp.message_handler(commands=('edit_data'))
async def edit_data(msg: types.Message):
    args = msg.get_args().split()
    if not args or len(args) < 3:
        await msg.answer(f'Используй: /edit_data [number(номер) / date_of_birth(дата рождения) / mail(почта)] [значние] [Фамилия Имя Отчество]')
        return
    
    column_name = args[0]
    value = args[1]
    name = ' '.join(args[2:])
    query = (f'''
        UPDATE `phonebook`
        SET {column_name} = ?
        WHERE name = ?
    ''')
    databot_db.cur.execute(query, (value, name,))
    databot_db.base.commit()
    await msg.answer(f'Вы успешно изменили значение {column_name} на {value} для {name}')

def register_handlers_edit_data(dp: Dispatcher):
    dp.register_message_handler(edit_data, commands=['edit_data'])