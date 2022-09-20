from cgitb import text
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp

from filters import IsPrivate
from states import Registration
from utils.misk import rate_limit
from utils.registration import read_file, validation
from keyboards import accept_kb, set_name_kb

start_text = 'Вы начали регистрацию\nВаше имя'
 
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), Command('start'))
async def command_start(message: types.Message):

    
    welcome = read_file('messages/welcome.txt')
    await message.answer(welcome, reply_markup=accept_kb)

@dp.callback_query_handler(text ='registration')
async def start_registration(callback: types.CallbackQuery):
    name = callback.from_user.first_name
    if validation(name):
        await callback.message.answer(
            start_text, reply_markup=set_name_kb(name)
        )
    else:
        await callback.message.answer(
            start_text
        )
    await callback.answer()
    await Registration.name.set()