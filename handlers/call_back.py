import sqlite3
import re
from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard, save_button
# from scraping.news_scraper import NewsScraper
# from scraping.async_news import AsyncScraper


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo ?",
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Python Developer 🐍"
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Mojo Developer 🔥"
    )


async def admin_call(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Привет мастер🐲"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Ты не мой мастер 🤬"
        )


# async def scraper_call(call: types.CallbackQuery):
#     scraper = NewsScraper()
#     data = scraper.parse_data()
#     for url in data[:5]:
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=f"https://24.kg/{url}"
#         )


async def async_scraper_call(call: types.CallbackQuery):
    data = await AsyncScraper().async_scrapers()
    links = AsyncScraper
    for link in data:
        await bot.send_message(chat_id=call.from_user.id, text=f"{link}", reply_markup=await save_button())


async def save_service_call(call: types.CallbackQuery):
    link = re.search(r'(https?://\S+)', call.message.text)
    if link:
        Database().sql_insert_servise_commands(link=link.group(0))

    await bot.send_message(chat_id=call.from_user.id, text="Вы сохранили ссылку")


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "mojo")
    dp.register_message_handler(admin_call,
                                lambda word: "dorei" in word.text)
    # dp.register_callback_query_handler(scraper_call,
    #                                    lambda call: call.data == "news")
    dp.register_callback_query_handler(async_scraper_call,
                                       lambda call: call.data == 'async_news')
    dp.register_callback_query_handler(save_service_call,
                                       lambda call: call.data == 'save_service')
