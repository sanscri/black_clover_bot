from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def admin_kb():
    kb_list = [
        [KeyboardButton(text="👤Список персонажей"), KeyboardButton(text="🎒Предметы")],
        [KeyboardButton(text="🧙Военный квартал")],
        [KeyboardButton(text="🔙Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def people_kb():
  kb_list = [
        [KeyboardButton(text="🎒Предметы экипировки"), KeyboardButton(text="♻️Ресурсы")],
        [KeyboardButton(text="🍧Еда и напитки"),  KeyboardButton(text="🍸Бары")],
        [KeyboardButton(text="🎒Настройки магазина"),KeyboardButton(text="🔙Назад")]
        ]
  return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def admin_items_kb():
    kb_list = [
        [KeyboardButton(text="👤Список персонажей"), KeyboardButton(text="🎒Предметы")],
        [KeyboardButton(text="🧙Военный квартал")],
        [KeyboardButton(text="🔙Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )


def admin_mondey_kb():
    kb_list = [
        [KeyboardButton(text="💸Все транзакци")],
        [KeyboardButton(text="💸Начислить деньги"), KeyboardButton(text="💸Оштрафовать")],
        [KeyboardButton(text="🔙Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
