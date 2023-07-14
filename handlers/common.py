from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inline import number_rock_magic_keyboard


common_router = Router()
@common_router.message(Command('start'))
async def start_command(message: Message):
    await message.answer('Привет! Я могу предложить вам сыграть в одну из игр.\n'
                         'Нажмите на одну из кнопок под этим сообщением',reply_markup=number_rock_magic_keyboard)
