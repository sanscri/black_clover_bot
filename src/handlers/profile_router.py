from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.formatting import Bold, as_line, as_list
from aiogram.fsm.state import StatesGroup, State

from keyboards.reply_profile_kb import profile_kb
profile_router = Router()



class ProfileStates(StatesGroup):
    content = State()  # Ожидаем любое сообщение от пользователя
    check_state = State()  # Финальна проверка



@profile_router.message(Command("profile"))
@profile_router.message(F.text == '👤Профиль')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
    name = "Тест"
    sex = ""
    age = ""
    state = ""
    race = ""
    userId = "" 
    magicType = ""
    health = ""
    level = ""
    sanity = ""
    magicPower = ""
    constitution = ""
    intelligence = ""
    wisdom = ""
    charisma = ""
    strength = ""
    crit_chance = ""
    crit_damage = ""
    content =  as_list(as_line(Bold("ПРОФИЛЬ")),
                        as_line(Bold("🆔Ваш id"), userId, end="", sep=": "),
                        as_line(Bold("🏷️Имя"), name, end="", sep=": "),
                        as_line(Bold("⚧Пол"), sex, end="", sep=": "), 
                        as_line(Bold("🌍Родина"), state, end="", sep=": "),
                        as_line(Bold("👤Раса"), race, end="", sep=": "),
                        as_line(Bold("🕐Возраст"), age, end="", sep=": "),
                        as_line(Bold("🃏Магический атрибут"), magicType, end="", sep=": "),
                        as_line(Bold("🏆Уровень персонажа"), level, end="", sep=": "),
                        as_line(Bold("♥️Здоровье"), health, end="", sep=": "),
                        as_line(Bold("🌀Магическая сила"), magicPower, end="", sep=": "),
                        as_line(Bold("🤪Здравомыслие"), sanity, end="", sep=": "),
                        as_line(Bold("⚔️Атака"), constitution, end="", sep=": "),
                        as_line(Bold("🛡️Защита"), intelligence, end="", sep=": "),
                        as_line(Bold("🏋️Телосложение"), constitution, end="", sep=": "),
                        as_line(Bold("🎓Интеллект"), intelligence, end="", sep=": "),
                        as_line(Bold("📚Мудрость"), wisdom, end="", sep=": "),
                        as_line(Bold("💪Сила"), strength, end="", sep=": "),
                        as_line(Bold("🗣Харизма"), charisma, end="", sep=": "),
                        as_line(Bold("🎯Шанс критического удара"), crit_chance, end="", sep=": "),
                        as_line(Bold("💥Урон от критического удара"), crit_damage, end="", sep=": "),
                        as_line(Bold("👛Кошелёк"), "🟤", "⚪️", "🔵", "🟡", "🪙", end="", sep=": "),
                        )
  
    await message.answer(**content.as_kwargs(), reply_markup=profile_kb())
    

@profile_router.message(F.text == '📕 Гримуар')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
 
    userId = "Тест"
    magicType = "Тест"
    content =  as_list(as_line(Bold("📕 Гримуар")),
                        as_line(Bold("🆔Ваш id"), userId, end="", sep=": "),
                        as_line(Bold("🃏Магический атрибут"), magicType, end="", sep=": "),
                        )
    await message.answer(**content.as_kwargs(), reply_markup=profile_kb())