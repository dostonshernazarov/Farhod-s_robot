import sqlite3

from data.config import ADMINS

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from filters import IsPrivate

from keyboards.inline.subscription import check_button
from utils.misc import subscription

from loader import dp, bot, db



@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: Message):
    name = message.from_user.full_name

    #foydalanuvchini bazaga qo'shish
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        pass

    await message.answer(f"Assalomu alaykum {message.from_user.full_name}.\n<a href='https://t.me/AbduholiqovFarhod'>Farhod's blog</a> kanalining robot botiga xush kelibsiz!", reply_markup=menu, disable_web_page_preview=True)

    # adminga habar berish
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} botga qo'shildi.\nBotda {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
