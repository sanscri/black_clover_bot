from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def main_map_kb():
    kb_list = [
        [KeyboardButton(text="⚔️ Арена"), KeyboardButton(text="🎯Тренировочная площадка")],
        [KeyboardButton(text="🍶 Бар"),  KeyboardButton(text="🎰Казино"), KeyboardButton(text="🕸 Черный рынок")],
        [KeyboardButton(text="🏰Башня гримуаров"), KeyboardButton(text="📚Библиотека"), KeyboardButton(text="🏥 Больница")],
        [KeyboardButton(text="⚒️Кузница"), KeyboardButton(text="🛠Мастерская"), KeyboardButton(text="⛏️Шахты"),  KeyboardButton(text="Природа")],
        [KeyboardButton(text="🔙 Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )



def main_house_kb():
    kb_list = [
        [KeyboardButton(text="🔙 Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )