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

help_router = Router()

@help_router.message(Command("help"))
async def cmd_start(message: Message, state: FSMContext):
  
    help = f"ℹ️ Информационная справка\n\nЭтот бот предназначен для игры в мире, основанном на манге \"Чёрный Клевер\" Юки Табаты. Важную информацию вы можете найти ниже. \n"
    await message.answer(help,
                              reply_markup=help_kb())
