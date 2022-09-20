from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import Registration 
from utils.registration import valid_weight
from keyboards import family_status_m_kb, family_status_f_kb

@dp.message_handler(Command('cancel'),state=Registration.weight)
async def cancel_get_name(message: Message, state: FSMContext):
    pass

@dp.message_handler(state=Registration.weight)
async def get_name(message: Message, state: FSMContext):
    weight = message.text
    if not valid_weight(weight):
        await message.answer('Введите правильное число\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(weight=weight)
    await send_family_status(state, message)
    await Registration.next()

async def send_family_status(state:FSMContext, message:Message):
    gender = (await state.get_data()).get('gender')
    if gender == 'Мужчина':
        await message.answer('Ваш семейный статус?', reply_markup=family_status_m_kb)
    else:
        await message.answer('Ваш семейный статус?', reply_markup=family_status_f_kb)