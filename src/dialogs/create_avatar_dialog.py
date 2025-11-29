from aiogram.types import CallbackQuery
from aiogram.filters.state import StatesGroup, State

from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.kbd import Button, Cancel, SwitchTo
from aiogram_dialog.widgets.text import Const, Format, Jinja
from aiogram.utils.formatting import Text, Bold, as_list, as_line
from create_bot import bot, dp, admins
from typing import Any

from aiogram_dialog.widgets.kbd import (
    Row
)

from database.dao import add_avatar, get_countries, get_races
from keyboards.reply_other_kb import main_kb



class CreateAvatarSG(StatesGroup):
    main = State()
    race = State()
    country = State()



async def to_race(callback: CallbackQuery, button: Button,
                    manager: DialogManager):
    dialog_data = manager.dialog_data
    race = await get_races(page=dialog_data["race_page"], items_per_page=1)
    manager.dialog_data["race_page_info"] = {
        "id": race[0]["id"],
        "name": race[0]["name"],
        "description": race[0]["description"],
    }
    await manager.switch_to(CreateAvatarSG.race)

async def to_country(callback: CallbackQuery, button: Button,
                    manager: DialogManager):
    dialog_data = manager.dialog_data
    country = await get_countries(page=dialog_data["country_page"], items_per_page=1)
    manager.dialog_data["country_page_info"] = {
        "id": country[0]["id"],
        "name": country[0]["name"],
        "description": country[0]["description"],
    }
    await manager.switch_to(CreateAvatarSG.country)

async def go_back(callback: CallbackQuery, button: Button,
                  manager: DialogManager):
    await manager.back()


async def cancel_dialog(callback: CallbackQuery, button: Button,
                  manager: DialogManager):
    chat_id = callback.message.chat.id
    country_id = manager.dialog_data["current_country"]["id"]
    race_id = manager.dialog_data["current_race"]["id"]
    avatar = await add_avatar(chat_id, race_id, country_id)
    if avatar is None:
        await callback.message.answer("Не удалось создать пользователя. Пожалуйста, обратитесь в техподдержку.")
        return
    #await manager.event.answer("hello")
    await callback.message.answer("✅ Сообщение отправлено", reply_markup=main_kb())
    await manager.done(result=avatar)
    
    #await manager.send_message(chat_id=chat_id, text="Профиль")
    #if avatar is None:
    #    fail_text = "Не удалось создать пользователя. Пожалуйста, обратитесь в техподдержку."



async def go_next(callback: CallbackQuery, button: Button,
                  manager: DialogManager):
    await manager.next()

async def get_previous_race(callback: CallbackQuery, button: Button, manager: DialogManager):
    dialog_data = manager.dialog_data

    if(dialog_data["race_page"] > 1):
        manager.dialog_data["race_page"] -= 1
    if(dialog_data["race_page"] <= 1):
        manager.dialog_data["previous_race_exist"] = False
        return
    manager.dialog_data["next_race_exist"] = True

    race = await get_races(page=dialog_data["race_page"], items_per_page=1)

    manager.dialog_data["race_page_info"] = {
        "id": race[0]["id"],
        "name": race[0]["name"],
        "description": race[0]["description"],
    }
    #manager.start_data["next_item_exist"] = item_number + 1 < len(items)
    #manager.start_data["previous_item_exist"] = item_number > 0 and len(items) > 1

async def get_next_race(callback: CallbackQuery, button: Button, manager: DialogManager):
    dialog_data = manager.dialog_data
    manager.dialog_data["race_page"] += 1
    if manager.dialog_data["next_race_exist"]:
        return
    race = await get_races(page=dialog_data["race_page"], items_per_page=1)
    manager.dialog_data["race_page_info"] = {
        "id": race[0]["id"],
        "name": race[0]["name"],
        "description": race[0]["description"],
    }
    
    manager.dialog_data["previous_race_exist"] = True
    manager.dialog_data["next_race_exist"] = manager.dialog_data["race_page"] < race[0]["count"]



async def get_previous_country(callback: CallbackQuery, button: Button, manager: DialogManager):
    dialog_data = manager.dialog_data

    if(dialog_data["country_page"] > 1):
        manager.dialog_data["country_page"] -= 1
    if(dialog_data["country_page"] <= 1):
        manager.dialog_data["previous_country_exist"] = False
        return
    manager.dialog_data["next_country_exist"] = True

    country = await get_countries(page=dialog_data["country_page"], items_per_page=1)

    manager.dialog_data["country_page_info"] = {
        "id": country[0]["id"],
        "name": country[0]["name"],
        "description": country[0]["description"],
    }
    #manager.start_data["next_item_exist"] = item_number + 1 < len(items)
    #manager.start_data["previous_item_exist"] = item_number > 0 and len(items) > 1

async def get_next_country(callback: CallbackQuery, button: Button, manager: DialogManager):
    dialog_data = manager.dialog_data
    manager.dialog_data["country_page"] += 1
    if manager.dialog_data["next_country_exist"]:
        return
    country = await get_countries(page=dialog_data["country_page"], items_per_page=1)
    manager.dialog_data["country_page_info"] = {
        "id": country[0]["id"],
        "name": country[0]["name"],
        "description": country[0]["description"],
    }
    print(manager.dialog_data["country_page"], country[0]["count"])
    manager.dialog_data["previous_country_exist"] = True
    manager.dialog_data["next_country_exist"] = manager.dialog_data["country_page"] < country[0]["count"]


async def choose_race(data: dict, widget: Whenable, manager: DialogManager):
    manager.dialog_data["current_race"] =  manager.dialog_data["race_page_info"] 
    await manager.switch_to(CreateAvatarSG.main)

async def choose_country(data: dict, widget: Whenable, manager: DialogManager):
    manager.dialog_data["current_country"] =  manager.dialog_data["country_page_info"] 
    await manager.switch_to(CreateAvatarSG.main)


async def on_dialog_start(start_data: Any, manager: DialogManager):

    manager.dialog_data["current_race"] = {
        "id": "",
        "name": "",
        "description": "",
    }
    manager.dialog_data["current_country"] = {
        "id": "",
        "name": "",
        "description": "",
    }

    manager.dialog_data["race_page_info"] = {
        "id": "",
        "name": "",
        "description": "",
    }
    manager.dialog_data["country_page_info"] = {
        "id": "",
        "name": "",
        "description": "",
    }
    manager.dialog_data["country_page"] = 1
    manager.dialog_data["race_page"] = 1
    manager.dialog_data["country_page"] = 1
    manager.dialog_data["next_race_exist"] = True
    manager.dialog_data["previous_race_exist"] = False

    manager.dialog_data["next_country_exist"] = True
    manager.dialog_data["previous_country_exist"] = False



def previous_race_exist(data: dict, widget: Whenable, manager: DialogManager):
    return manager.dialog_data["previous_race_exist"]

def next_race_exist(data: dict, widget: Whenable, manager: DialogManager):
     return  manager.dialog_data["next_race_exist"]


def previous_country_exist(data: dict, widget: Whenable, manager: DialogManager):
    return manager.dialog_data["previous_country_exist"]

def next_country_exist(data: dict, widget: Whenable, manager: DialogManager):
     return  manager.dialog_data["next_country_exist"]


async def get_data(dialog_manager: DialogManager, **kwargs) -> dict[str, Any]:
    # Retrieve data from dialog_data
    current_race = dialog_manager.dialog_data.get("current_race")
    current_country = dialog_manager.dialog_data.get("current_country")
    return {"current_race": current_race["name"], "current_country": current_country["name"]}


avatar_info = Jinja("""
<b>Ваш персонаж</b>
                    
<b>👤Раса:</b> {{current_race}}
<b>🌍Родина:</b> {{current_country}}
""")

create_avatar_window = Window(
    avatar_info,  
    Button(Const("Раса"), id="race", on_click=to_race), 
    Button(Const("Страна"), id="country", on_click=to_country),
    Cancel(Const("Сохранить"), id="save", on_click=cancel_dialog), 
    parse_mode="HTML",
    state=CreateAvatarSG.main, 
    getter=get_data,
)

choose_race_window = Window(
        Format("{dialog_data[race_page_info][name]}"),
        Row( Button(
                Const("Выбрать"),
                id="choose_race",
                on_click=choose_race,
            ),),
         Row(
            Button(
                Const("<-"),
                id="previous_race",
                when=previous_race_exist,
                on_click=get_previous_race,
            ),
            Button(
                Const("->"),
                id="next_race",
                when=next_race_exist,
                on_click=get_next_race,
            ),
        ),
        Button(Const("🔙Назад"), id="race_back", on_click=go_back),
        parse_mode="HTML",
        state=CreateAvatarSG.race,
    )

choose_country_window = Window(
        Const("Страна"),

        Format("{dialog_data[country_page_info][name]}"),
        Row(
            Button(
                Const("Выбрать"),
                id="choose_country",
                on_click=choose_country,
            ),
        ),
         Row(

            Button(
                Const("<-"),
                id="previous_country",
                when=previous_country_exist,
                on_click=get_previous_country,
            ),
            Button(
                Const("->"),
                id="next_country",
                when=next_country_exist,
                on_click=get_next_country,
            ),
        ),
        SwitchTo(Const("🔙Назад"), id="country_back", state=CreateAvatarSG.main),
        state=CreateAvatarSG.country,
    )
create_avatar_dialog = Dialog(
    create_avatar_window,
    choose_race_window,
    choose_country_window,
    on_start=on_dialog_start
)