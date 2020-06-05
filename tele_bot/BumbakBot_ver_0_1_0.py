from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
import logging
from tele_bot.bot_module import get_info
from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(level=logging.INFO)
bot = Bot(config.token)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

available_year_names = ["2016", "2017", "2018", "2019", "2020"]
available_room_numbers = ["1", "2", "3", "4", "all"]


class my_make_query(StatesGroup):
    waiting_for_year_name = State()
    waiting_for_room_number = State()
    waiting_for_street_name = State()


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message):
    await message.answer('Hello ' + str(message.from_user.first_name), reply_markup=types.ReplyKeyboardRemove())
    if message.from_user.id in config.available_user_id:
        await message.answer('You can start work with command \n /real')
        print(message.from_user.id)
    else:
        await message.answer('ACCESS DENIED')
        await message.answer('Call to support')
        print(message.from_user.id)


@dp.message_handler(commands="real", state="*")
async def year_step_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for year in available_year_names:
        keyboard.add(year)
    await message.answer("Enter year:", reply_markup=keyboard)
    await my_make_query.waiting_for_year_name.set()


@dp.message_handler(state=my_make_query.waiting_for_year_name, content_types=types.ContentTypes.TEXT)
async def room_step_2(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for room in available_room_numbers:
        keyboard.add(room)
    await message.answer("Enter number of rooms:", reply_markup=keyboard)
    await my_make_query.waiting_for_room_number.set()
    await state.update_data(year=message.text.lower())


@dp.message_handler(state=my_make_query.waiting_for_room_number, content_types=types.ContentTypes.TEXT)
async def street_step_3(message: types.Message, state: FSMContext):
    await message.answer("Enter street name:", reply_markup=types.ReplyKeyboardRemove())
    await my_make_query.waiting_for_street_name.set()
    await state.update_data(room=message.text.lower())


@dp.message_handler(state=my_make_query.waiting_for_street_name, content_types=types.ContentTypes.TEXT)
async def query_step_4(message: types.Message, state: FSMContext):
    await state.update_data(street=message.text.lower())
    user_data = await state.get_data()
    await message.answer("Your query to DB:" + "\n" +
                         user_data['year'] + "\n" +
                         user_data['room'] + "\n" +
                         user_data['street'] + "\n"
                         , reply_markup=types.ReplyKeyboardRemove())
    print(user_data, message.from_user.id)
    await state.finish()
    a = get_info.find_data(user_data['year'], user_data['street'], user_data['room'])
    if len(a) == 0:
        await message.answer("Info not found. Try to check is the [street name] is correct")
    print(a)
    for i in a:
        month = i[0]
        city = i[1]
        district = i[2]
        street = i[3]
        house_number = i[4]
        number_of_rooms = i[5]
        floor = i[6]
        total = i[7]
        characteristic = i[8]
        price_all = i[9]
        price_per_sq_m = i[10]
        comments = i[11]

        last_ver = "[Month] " + str(month) + "\n[City / Village] " + str(city) + "\n[District] " + str(district) + \
                   "\n[Street / Residential complex]" + str(street) + "\n[House number]" + str(house_number) + \
                   "\n[Number of rooms]" + str(number_of_rooms) + \
                   "\n[Floor / Floors]" + str(floor) + "\n[Total area]" + str(total) + "\n[Characteristic]" + \
                   str(characteristic) + "\n[Price / all, $]" + str(price_all) + "'\n[Price / per sq.m, $]" + \
                   str(price_per_sq_m) + "\n[Comments] " + str(comments)
        await message.answer(last_ver)
    await message.answer("Type: /real to resume")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
