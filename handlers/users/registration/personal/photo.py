from aiogram.types import Message, ContentType, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from utils import get_photo_id
from keyboards.registration.gender_kb import gender_kb

from loader import dp, db
from states import Registration 



@dp.message_handler(state=Registration.photo)
async def state1(message: Message, state: FSMContext):
    await message.answer('Отправьте фотографию, а не текст\nесли хотите прервать регистрацию, нажмите /cancel', reply_markup=ReplyKeyboardRemove(selective=False))
    return

@dp.message_handler(content_types=ContentType.PHOTO,state=Registration.photo)
async def get_photo(message: Message, state: FSMContext):
    photo_id = get_photo_id(message)
    await state.update_data(photo=photo_id)
    response = await create_user(state)
    if response:
        await message.answer('Вы успешно зарегестрированы', reply_markup=ReplyKeyboardRemove(selective=False))
        await state.finish()
        return 
    await message.answer('Что-то пошло не так, попробуйте снова', reply_markup=ReplyKeyboardRemove(selective=False))

    
async def create_user(state: FSMContext):
    id, name, gender, birthday, city, description, photo =  await get_data(state=state)
    try:

        response = await db.create_user({
            '_id': id,
            'name': name,
            'gender': gender,
            'birthday': birthday,
            'city': city,
            'description': description,
            'photo': photo,
            'status': 'active'
        })
        return response
    except Exception as e:
        print(e)
        return {}
    
async def get_data(state: FSMContext):
    data = await state.get_data()
    id, name, gender, birthday, city, description, photo = data.get('id'), data.get('name'), data.get('gender'), data.get('birthday'), data.get('city'), data.get('description'), data.get('photo')
    return id, name, gender, birthday, city, description, photo