from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from database.dao import set_user
from keyboards.reply_other_kb import main_kb
from aiogram.types import FSInputFile
from create_bot import bot, dp, admins
from pathlib import Path
from create_bot import logger
from settings import settings
from filters.chat_type import ChatTypeFilter
start_router = Router()



@start_router.message(F.text == '🔙Назад')
@start_router.message(ChatTypeFilter(chat_type=["private"]),CommandStart())
async def cmd_private_start(message: Message, state: FSMContext):
    await state.clear()
    BASE_DIR = Path(__file__).parent.parent.parent
    WELCOME_IMAGE_PATH = BASE_DIR / "assets" / "hello.jpg"
    user = await set_user(tg_id=message.from_user.id,
                          username=message.from_user.username,
                          full_name=message.from_user.full_name)
    greeting = f"Привет, {message.from_user.full_name}! Выбери необходимое действие"
    if user is None:
        greeting = f"Великая война, затронувшая все 4 королевства мира Чёрного клевера, закончилась 300 лет назад.\n\nВойска Люциуса Зогратиса тогда потерпели поражение в битве за столицу Королевства Клевер. Жизнь возвратилась в мирное русло, а о героях той войны, Асте и Юно, стали слагать легенды.\nОднако на горизонте появилась новая угроза.\n\nИз дальних уголков всех четырёх королевств доходят слухи о странных подземельях, оставленных далёкими предками, жившими тысячилетия назад на этой земле, о разломах, порождающих невиданных чудовищ, а также о появленнии новых Великих Магических Зон на нейтральных территориях, в которых очень опасно находиться.\n\nCейчас после той великой войны судьба дала жителям мира Чёрного клевера передышку, но надолго ли?\n\nСможете ли вы повлиять на исход будущих событий и встать в один ряд с сильными мира сего? Все в ваших руках…"

    photo = FSInputFile(WELCOME_IMAGE_PATH)
    await message.answer_photo(photo=photo, caption=greeting, reply_markup=main_kb())

@start_router.message(ChatTypeFilter(chat_type=["group", "supergroup"]),CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    greeting = f"Привет, путник!"
    await message.answer(greeting, reply_markup=ReplyKeyboardRemove())

@start_router.message(F.text == '❌ Остановить сценарий')
async def stop_fsm(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Сценарий остановлен. Для выбора действия воспользуйся клавиатурой ниже",
                         reply_markup=main_kb())


@start_router.callback_query(F.data == 'main_menu')
async def main_menu_process(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer('Вы вернулись в главное меню.')
    await call.message.answer(f"Привет, {call.from_user.full_name}! Выбери необходимое действие",
                              reply_markup=main_kb())



# Функция проверки подписки
async def is_subscribed(user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        logger.error(f"Error checking subscription: {e}")
        return False


# Клавиатура для подписки
def get_subscribe_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подписаться на канал", url=settings.CHANNEL_URL),
                InlineKeyboardButton(text="✅ Я подписался", callback_data="check_sub")
            ]
        ]
    )