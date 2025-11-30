from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.reply_map_kb import main_house_kb, main_map_kb


house_router = Router()

@house_router.message(F.text == '🏠Дом')
@house_router.message(Command("house"))
async def cmd_profile(message: Message, state: FSMContext):
    text ='''
У тебя сейчас нет своего дома.

Для дома необходим участок, который можно приобрести в городской администрации.

Сам 🛖дом можно построить через мастерскую или купить.'''
    await message.answer(text, reply_markup=main_house_kb())
    
    