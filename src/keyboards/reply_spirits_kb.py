from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def devil_kb():
    kb_list = [
        [KeyboardButton(text="Назад🔙Назад")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
