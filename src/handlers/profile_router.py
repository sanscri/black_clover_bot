from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.formatting import Bold, as_line, as_list
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from keyboards.reply_profile_kb import contracts_kb, effects_kb, grimoire_kb, inventory_kb, profile_kb, skills_kb, stats_kb
profile_router = Router()



class ProfileStates(StatesGroup):
    pass



@profile_router.message(Command("profile"))
@profile_router.message(F.text == '🧙 Основное')
@profile_router.message(F.text == '👤 Профиль')
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
    motivation = ""
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
                        as_line(Bold("⚡️ Мотивация"), motivation, end="", sep=": "),
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
                        ).as_html()
  
    await message.answer(content, parse_mode=ParseMode.HTML, reply_markup=profile_kb())
    

@profile_router.message(F.text == '📕 Гримуар')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
 
    userId = "Тест"
    magicType = "Тест"
    content =  as_list(as_line(Bold("📕 Гримуар")),
                        as_line(Bold("🆔Ваш id"), userId, end="", sep=": "),
                        as_line(Bold("🃏Магический атрибут"), magicType, end="", sep=": "),
                        )
    await message.answer(content.as_html(), parse_mode=ParseMode.HTML, reply_markup=grimoire_kb())


@profile_router.message(F.text == '🧬 Характеристики')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
 

    content =  as_list(as_line(Bold("🧬 Характеристики")),
                        )
    await message.answer(content.as_html(), parse_mode=ParseMode.HTML, reply_markup=stats_kb())


@profile_router.message(F.text == '📖 Навыки')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
 
    content =  as_list(as_line(Bold("📖 Навыки")))
    await message.answer(content.as_html(), parse_mode=ParseMode.HTML, reply_markup=skills_kb())



@profile_router.message(F.text == '🎒 Инвентарь')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
 
    content =  as_list(as_line(Bold("🎒 Инвентарь"))
                        )
    await message.answer(content.as_html(), parse_mode=ParseMode.HTML, reply_markup=inventory_kb())


@profile_router.message(F.text == '🪄 Эффекты')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
 

    content =  as_list(as_line(Bold("🪄 Эффекты")),
                        )
    await message.answer(content.as_html(), parse_mode=ParseMode.HTML, reply_markup=effects_kb())

@profile_router.message(F.text == '📃 Контракты')
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
 
    content =  as_list(as_line(Bold("📃 Контракты")),
                        )
    await message.answer(content.as_html(), parse_mode=ParseMode.HTML, reply_markup=contracts_kb())