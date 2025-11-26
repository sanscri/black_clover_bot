from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.formatting import Text, Bold, as_line, as_list

from keyboards.reply_profile_kb import main_profile_kb

map_router = Router()

@map_router.message(Command("map"))
async def cmd_profile(message: Message, state: FSMContext):
    text = "Карта"
    await message.answer(text)
    