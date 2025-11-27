from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

aincrad_router = Router()



def get_battle_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[

            [InlineKeyboardButton(text="Бросить вызов", callback_data="try_descent"),
             InlineKeyboardButton(text="Вернуться", callback_data="return_to_menu")]
        ]
    )

@aincrad_router.message(Command("dungeon"))
async def cmd_profile(message: Message, state: FSMContext):
    await message.answer("🚪 Подземелье сегодня не работает...")
    await message.answer(
                f"Этаж",
                reply_markup=get_battle_keyboard()
            )


@aincrad_router.message(Command("labyrinth"))
async def cmd_profile(message: Message, state: FSMContext):
    await message.answer("Вы готовы войти в Лабиринт?")
    buttons = [
        [KeyboardButton(text="🧩Войти в лабиринт")],
        [KeyboardButton(text="🔙Назад")],
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("Лабиринт:", reply_markup=markup)
    