from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def devil_kb():
    kb_list = [
        [KeyboardButton(text="Список дьяволов по рангам")],
        [KeyboardButton(text="Список дьяволов по этажам")],
        [KeyboardButton(text="🔙Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def devil_rank_kb():
    kb_list = [
        [KeyboardButton(text="Высшие дьяволы")],
         [KeyboardButton(text="Высокоранговые дьявол")],
         [KeyboardButton(text="Среднеранговые дьяволы")],
         [KeyboardButton(text="Низкоранговые дьяволы")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def devil_floor_kb():
    kb_list = [
        [KeyboardButton(text="Первый этаж")],
        [KeyboardButton(text="Второй этаж")],
        [KeyboardButton(text="Третий этаж")],
        [KeyboardButton(text="Четвёртый этаж")],
        [KeyboardButton(text="Пятый этаж")],
        [KeyboardButton(text="Шестой этаж")],
        [KeyboardButton(text="Седьмой этаж")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
