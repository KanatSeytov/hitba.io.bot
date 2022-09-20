import certifi
import ssl
from geopy.geocoders import Nominatim
from aiogram.types import Message, CallbackQuery
import geopy.geocoders
from geopy.geocoders import Nominatim
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import Registration 

geoLocator = Nominatim(user_agent='geoapiExercises', scheme='http')

@dp.message_handler(Command('cancel'),state=Registration.city)
async def cancel_get_name(message: Message, state: FSMContext):
    print('asd')
    pass

# @dp.message_handler(state=Registration.location)

@dp.message_handler(content_types=['location'], state=Registration.city)
async def get_name(message: Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude

    location = geoLocator.reverse(f'{lat},{lon}')
    address = location.raw['address']
    city = address.get('city','')
    await state.update_data(city=city)
    await message.answer(f'вы проживаете в городе {city}')
    await message.answer(f'Расскажите о себе, ваши интересы, чего вы ожидаете от брака и что бы хотели указать дополнительно')
    await Registration.next()
