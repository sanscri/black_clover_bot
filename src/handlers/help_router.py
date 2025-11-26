from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.reply_help_kb import help_kb

help_router = Router()

@help_router.message(Command("help"))
async def cmd_start(message: Message, state: FSMContext):
  
    help = f"""
    ℹ️ Информационная справка
    Этот бот предназначен для игры в мире, основанном на манге \"Чёрный Клевер\" Юки Табаты. 
    Важную информацию вы можете найти ниже.
    """
    await message.answer(help,
                              reply_markup=help_kb())