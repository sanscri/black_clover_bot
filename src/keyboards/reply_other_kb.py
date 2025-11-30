from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_kb():
    kb_list = [
         [KeyboardButton(text="🌍Начать путешествие")],
         [ KeyboardButton(text="📖Справочник")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )


def main_kb():
    kb_list = [
        [KeyboardButton(text="👤 Профиль"), KeyboardButton(text="🗺Карта")],
        [KeyboardButton(text="🏠Дом"), KeyboardButton(text="📜Доска почёта"), KeyboardButton(text="❓Помощь")]
    ]

    
    '''
    kb_list = [
        [KeyboardButton(text="👤 Профиль"), KeyboardButton(text="🗺Карта")],
        [KeyboardButton(text="🧚‍♀️Духи"), KeyboardButton(text="😈Дьяволы")],
        [KeyboardButton(text="📜Объявления"), KeyboardButton(text="📜Квесты"),  KeyboardButton(text="❓Помощь")]
    ]
    '''
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )


def honor_board_kb():
    kb_list = [
        [KeyboardButton(text="⚜️ Титулы"), KeyboardButton(text="🧩 Коллекции")],
        [KeyboardButton(text="📈 Статистика"), KeyboardButton(text="🏆 Топ")],
        [KeyboardButton(text="🔙 Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
