from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.reply_help_kb import help_kb

shop_router = Router()

@shop_router.message(Command("shop"))
async def cmd_shop(message: Message, state: FSMContext):
  
    help = f"""
    ℹ️ Информационная справка
    Этот бот предназначен для игры в мире, основанном на манге \"Чёрный Клевер\" Юки Табаты. 
    Важную информацию вы можете найти ниже.
    """
    await message.answer(help,
                              reply_markup=help_kb())