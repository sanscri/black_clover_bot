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
        [KeyboardButton(text="👤Профиль"), KeyboardButton(text="🏢Организации")],
         [KeyboardButton(text="🧚‍♀️Духи"), KeyboardButton(text="😈Дьяволы")],
          [KeyboardButton(text="📜Объявления"), KeyboardButton(text="📜Квесты"),  KeyboardButton(text="❓Помощь")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def stop_fsm():
    kb_list = [
        [KeyboardButton(text="❌ Остановить сценарий")],
        [KeyboardButton(text="🏠 Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Для того чтоб остановить сценарий FSM нажми на одну из двух кнопок👇"
    )


