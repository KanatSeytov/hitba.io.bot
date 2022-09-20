from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from loader import dp
from states import Registration 
from utils.registration import validation


@dp.message_handler(Command('cancel'),state=Registration.description)
async def cancel_get_name(message: Message, state: FSMContext):
    pass

@dp.message_handler(state=Registration.description)
async def get_name(message: Message, state: FSMContext):
    desciption = message.text
    await state.update_data(desciption=desciption)
    # -----------------
    await message.answer('Отправьте свою фотографию')
    await Registration.next()

