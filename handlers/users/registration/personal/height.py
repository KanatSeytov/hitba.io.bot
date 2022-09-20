from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import Registration 
from utils.registration import valid_height


@dp.message_handler(Command('cancel'),state=Registration.height)
async def cancel_get_name(message: Message, state: FSMContext):
    pass

@dp.message_handler(state=Registration.height)
async def get_name(message: Message, state: FSMContext):
    height = message.text
    if not valid_height(height):
        await message.answer('Введите правильное число\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(height=height)
    await message.answer('Ваш вес?')
    await Registration.next()


