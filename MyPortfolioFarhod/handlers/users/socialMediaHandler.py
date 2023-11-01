from aiogram.dispatcher.filters import Command, Text
# from keyboards.default.socialMediaKeyboard import socialMedia 
from keyboards.inline.socialMedia import socialMedia_menu
from keyboards.inline.callback_Data import socialMedia_callback
from filters.private_chat import IsPrivate

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from loader import dp



@dp.message_handler(IsPrivate(), text="🌐 Social media")
async def socialMedia(message: Message):
    await message.answer("Kerakli tugmani tanlang", reply_markup=socialMedia_menu)
