from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_profile_kb():
    kb_list = [
        [KeyboardButton(text="Характеристики"), KeyboardButton(text="Ремесло")],
        [KeyboardButton(text="Инвентарь"), KeyboardButton(text="Навыки")],
        [KeyboardButton(text="Задания"), KeyboardButton(text="Достижения")],
        [KeyboardButton(text="Дом"), KeyboardButton(text="Задания")],
        [KeyboardButton(text="🔙Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )