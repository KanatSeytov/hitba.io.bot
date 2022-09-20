from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    # personal data
    id = State()
    name = State()
    gender = State()
    birthday = State()
    city = State()
    description = State()
    photo = State()

    # finish_personal_data = State()

    # # religion
    # pray = State()
    # food = State()
    # clothes = State()
    # quran = State()

    # finish_religion_data = State()

    # # dunia
    # job = State()
    # salary = State()
    # housing = State()
    # graduation_year = State()

    # finish_dunia_data = State()

    # # health
    # smoking = State()
    # alcohol = State()
    # diseases = State() # write concrete type if exist
    # healthy_food = State()
    # sport = State()

    # finish_health_data = State()
 