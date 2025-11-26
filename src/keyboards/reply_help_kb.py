from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from settings import settings
def help_kb():
    kb_list = [
        [InlineKeyboardButton(text="📚 База знаний", url=settings.TUTORIAL_URL), InlineKeyboardButton(text="📯 Игровые новости", url=settings.CHANNEL_URL)],
        [InlineKeyboardButton(text="💬 Общение", url=settings.GROUP_URL), InlineKeyboardButton(text="📨Баги и предложения", url=settings.SUPPORT_URL)],
        [InlineKeyboardButton(text="❗️Правила", url=settings.RULES_URL)]

    ]
    return InlineKeyboardMarkup(
        inline_keyboard=kb_list
    )

