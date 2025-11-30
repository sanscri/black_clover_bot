from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.reply_map_kb import main_map_kb


map_router = Router()

@map_router.message(F.text == '🗺Карта')
@map_router.message(Command("map"))
async def cmd_profile(message: Message, state: FSMContext):
    text = "Карта"
    await message.answer(text, reply_markup=main_map_kb())
    
    