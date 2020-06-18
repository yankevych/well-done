from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
import logging
from aiogram import Bot, Dispatcher, types, executor

from selenium import webdriver

logging.basicConfig(level=logging.INFO)
bot = Bot(config.token)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)


def get_data(x):
    # save screen to file and return it to user
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    my_url = 'https://' + x
    driver.get(my_url)

    size = lambda z: driver.execute_script('return document.body.parentNode.scroll' + z)
    driver.set_window_size(size('Width'), size('Height'))

    # save to where bot.py is / override every time
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

    driver.quit()
    b = open('web_screenshot.png', 'rb')
    return b


class my_make_query(StatesGroup):
    # to save and check "state"
    waiting_for_site = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Hello to user and take "site"
    await message.answer('Hello ' + str(message.from_user.first_name), reply_markup=types.ReplyKeyboardRemove())
    await message.answer('Enter site you want to download f.e. alpha-bots.com')
    await my_make_query.waiting_for_site.set()


@dp.message_handler(state=my_make_query.waiting_for_site, content_types=types.ContentTypes.TEXT)
async def query_step_1(message: types.Message, state: FSMContext):
    # Check input from user and do main work
    await state.update_data(site=message.text.lower())
    user_data = await state.get_data()
    a = get_data(user_data['site'])
    await message.answer_photo(a)
    await state.finish()
    await message.answer('You can start the new dialog with command /start')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
