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
@dp.message_handler(IsPrivate(), Command('update'))
async def command_start(message: types.Message):
    name = message.from_user.first_name
    if validation(name):
         await message.answer(
            text='Обновление профиля\nВаше имя', reply_markup=set_name_kb(name)
        )
    else:
        await message.answer(
            text='Обновление профиля\nВаше имя'
        )
    await Registration.name.set()