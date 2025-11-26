from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from database.dao import set_user
from keyboards.reply_help_kb import help_kb
from keyboards.reply_other_kb import main_kb
from aiogram.types import FSInputFile
from create_bot import bot, dp, admins
from pathlib import Path

from keyboards.reply_profile_kb import main_profile_kb

grimoire_router = Router()

@grimoire_router.message(Command("grimoire"))
async def cmd_grimoire(message: Message, state: FSMContext):
  
    info = f"""
    Гримуар
    """
    await message.answer(info,
                              reply_markup=help_kb())