from aiogram import types
from loader import dp
from model import show, load, find
from keybrd import kb_help

HELP_CMD = '''
<b>/show</b> - <em>Показать контакты</em>
<b>/find</b> - <em>Найти контакт(поисковый запрос через пробел после команды)</em>
<b>/help</b> - <em>Список команд</em>
<b>/start</b> - <em>Запуск бота</em>'''
path = 'database.csv'

@dp.message_handler(commands=['start'])
async def help_cmd(message: types.Message):
    await message.answer(text='Добро пожаловать в телефонный справочник!', reply_markup=kb_help)

@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.answer(text=HELP_CMD, parse_mode='HTML')
    
   
@dp.message_handler(commands=['show'])
async def show_cmd(message: types.Message):  
    await message.answer(text=show(load(path)), parse_mode='HTML')
    
@dp.message_handler(commands=['find'])
async def find_cmd(message: types.Message):
    f_str = message.text.split()[1]
    await message.answer(text=find(load(path), f_str), parse_mode='HTML')
    