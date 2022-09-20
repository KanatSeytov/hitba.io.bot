from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from loader import dp
from states import Registration 
from utils.registration import validation
from keyboards import gender_kb, has_children_kb
from data import f_statuses, m_statuses

@dp.message_handler(Command('cancel'),state=Registration.marriage_plan)
async def cancel_get_name(message: Message, state: FSMContext):
    pass

@dp.message_handler(state=Registration.marriage_plan)
async def get_name(message: Message, state: FSMContext):
    family_status = message.text
    if family_status not in (m_statuses+f_statuses):
        await message.answer('Введите правильный статус\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(family_status=family_status)
    # ---------------
    await message.answer('Есть ли у вас дети?', reply_markup=has_children_kb)
    await Registration.next()

@dp.callback_query_handler(state=Registration.marriage_plan)
async def get_marrige_plan(callback: CallbackQuery, state: FSMContext):
    marriage_plan = callback.data
    print(marriage_plan)
    # if marriage_plan not in (m_statuses+f_statuses):
    #     await callback.answer('Введите правильный статус\nесли хотите прервать регистрацию, нажмите /cancel')
    #     return
    # await state.update_data(marriage_plan=marriage_plan)
    # # -----------------
    # await callback.message.answer('Опишите себя и кого вы ищете')
    # await Registration.next()

