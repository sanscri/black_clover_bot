from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


map_router = Router()

@map_router.message(Command("map"))
async def cmd_profile(message: Message, state: FSMContext):
    text = "Карта"
    await message.answer(text)
    