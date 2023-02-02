from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_help = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
kb_help.add(b1)