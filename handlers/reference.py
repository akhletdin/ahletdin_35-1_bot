import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from const import REFERENCE_MENU_TEXT
from aiogram.utils.deep_linking import _create_link
from keyboards.inline_buttons import reference_menu_keyboard
import binascii
import os


async def reference_menu_call(call: types.CallbackQuery):
    db = Database()
    data = db.sql_select_balance_count_referral(
        tg_id=call.from_user.id
    )
    print(data)

    await bot.send_message(
        chat_id=call.from_user.id,
        text=REFERENCE_MENU_TEXT.format(
            username=call.from_user.username,
            balance=data['balance'],
            referral=data['count']
        ),
        reply_markup=await reference_menu_keyboard()
    )


async def reference_link_call(call: types.CallbackQuery):
    db = Database()
    user = db.sql_select_user(
        telegram_id=call.from_user.id
    )
    print(user)
    if not user['link']:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link(link_type="start", payload=token)
        db.sql_update_reference_link(
            link=link,
            owner=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Вот ваша новая ссылка: {link}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Вот ссылка на вашу базу данных: {user['link']}"
        )


async def reference_list_call(call: types.CallbackQuery):
    db = Database()
    user = db.sql_select_user(
        telegram_id=call.from_user.id
    )
    if user:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=user
        )
    else:
        await bot.send_message(chat_id=call.from_user.id,
                               text="нет пользователя")


def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(reference_menu_call,
                                       lambda call: call.data == "reference_menu")
    dp.register_callback_query_handler(reference_link_call,
                                       lambda call: call.data == "reference_link")
    dp.register_callback_query_handler(reference_list_call,
                                       lambda call: call.data == "reference_list")
