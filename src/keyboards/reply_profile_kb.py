from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def profile_kb():
    kb_list = [
        [KeyboardButton(text="📕 Гримуар"), KeyboardButton(text="⚙️ Статы"), KeyboardButton(text="🛠 Ремесло")],
        [KeyboardButton(text="📃 Контракты"),  KeyboardButton(text="👛 Кошелёк"), KeyboardButton(text="🎒 Инвентарь")],
        [KeyboardButton(text="📖 Навыки"), KeyboardButton(text="🏆 Достижения"), KeyboardButton(text="🏠 Дом")],
        [KeyboardButton(text="👤Профиль"), KeyboardButton(text="🔙Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )