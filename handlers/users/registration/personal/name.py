from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from loader import dp
from states import Registration 
from utils.registration import validation
from keyboards import send_location_kb, gender_kb


@dp.message_handler(Command('cancel'),state=Registration.name)
async def cancel_get_name(message: Message, state: FSMContext):
    pass


@dp.callback_query_handler(state=Registration.name)
async def get_family_status(callback: CallbackQuery, state: FSMContext):
    name = callback.data

    if not validation(name):
        await callback.answer('Вы ввели имя в неправильной форме\nвведите текст без чисел и специфичных символов\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(name=name)
    print(callback.message.chat.id)
    await state.update_data(id=callback.message.chat.id)
    # -----------------
    # await callback.message.answer('От куда вы?', reply_markup=send_location_kb)
    # await callback.answer()
    # await Registration.next()
    await callback.message.answer('Ваш пол?', reply_markup=gender_kb)
    await Registration.next()


@dp.message_handler(state=Registration.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    if not validation(name):
        await message.answer('Вы ввели имя в неправильной форме\nвведите текст без чисел и специфичных символов\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(name=name)
    await state.update_data(id=message.from_user.id)
    # -----------------
    await message.answer('Ваш пол?', reply_markup=gender_kb)
    await Registration.next()


    # await message.answer('От куда вы?', reply_markup=send_location_kb)
    # await Registration.location.set()

