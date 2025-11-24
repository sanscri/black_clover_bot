
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def squad_kb():
    kb_list = [
        [KeyboardButton(text="📊Ранги"), KeyboardButton(text="📔 Заявки"), KeyboardButton(text="👤Управление людьми")],
        [KeyboardButton(text="🛡Управление отрядами"), KeyboardButton(text="🧙Информация об армиях")]
        [KeyboardButton(text="🔙Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

