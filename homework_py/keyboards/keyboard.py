from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_help = KeyboardButton("/help")
button_list = KeyboardButton("/show_list")
button_add_people = KeyboardButton("/add_people")
button_dell_people = KeyboardButton("/dell_people")

kb_but = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_but.row(button_help, button_list).row(button_add_people, button_dell_people)