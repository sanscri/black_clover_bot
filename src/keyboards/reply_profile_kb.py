from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



'''
    kb_list = [
        [KeyboardButton(text="⚙️ Статы"), KeyboardButton(text="🛠 Ремесло")],
        [ KeyboardButton(text="👛 Кошелёк"), KeyboardButton(text="🎒 Инвентарь"), KeyboardButton(text="🧩 Коллекции")],
        [KeyboardButton(text="⚜️ Титулы"), KeyboardButton(text="🎏 Боевые приемы")
        [KeyboardButton(text="🥇 Ачивки"), KeyboardButton(text="📈 Статистика"), KeyboardButton(text="🏆 Топ")
    ]
'''


def profile_kb():
    kb_list = [
        [KeyboardButton(text="📕 Гримуар"), KeyboardButton(text="🧬 Характеристики"), KeyboardButton(text="📖 Навыки")],
        [KeyboardButton(text="🎒 Инвентарь"), KeyboardButton(text="🪄 Эффекты"), KeyboardButton(text="📃 Контракты")],
        [KeyboardButton(text="🧙 Основное"), KeyboardButton(text="🔙 Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def grimoire_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )


def grimoire_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )


def stats_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )


def skills_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def inventory_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def effects_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def contracts_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
