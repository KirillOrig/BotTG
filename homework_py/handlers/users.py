from aiogram import types

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(f'Привет! Я бот, который запоминает номера и еще некоторые данные человека.', reply_markup=kb_but)

@dp.message_handler(commands=["help"])
async def help(msg: types.Message):
    await msg.answer(f'<b>Вот список всех моих команд:</b>\n\
/start - начало работы с ботом\n\
/help - показать список команд\n\
/add_people - добавить человека в список\n\
/edit_data - редактировать данные человека\n\
/dell_data - удалить данные человека\n\
/dell_people - удалить человека из списка\n\
/show_list - показать телефонную книгу\n\
/find_people - найти данные о человеке\n\
')

@dp.message_handler(commands=["show_list"])
async def show_list(msg: types.Message):
    await msg.answer(f'<b>Вот Ваша телефонная книга:</b>\n\
')