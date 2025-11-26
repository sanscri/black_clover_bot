from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.reply_help_kb import help_kb
battle_router = Router()

# Клавиатура для подписки
def battle_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Найти противника", callback_data="find_opponent"),
            ],
            [
                 InlineKeyboardButton(text="Пригласить на бой", callback_data="invite_to_fight"),
            ]
        ]
    )

@battle_router.message(Command("fight"))
async def cmd_start(message: Message, state: FSMContext):
  
    text = f"🏟 Добро пожаловать на Алмазную Арену! Здесь ты можешь сразиться с другими игроками и получить высший боевой ранг."
    await message.answer(text,
                              reply_markup=battle_keyboard())