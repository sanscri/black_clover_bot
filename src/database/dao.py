from create_bot import logger
from .base import connection
from .models import Grimoire, User, Avatar, AvatarStats, Race, Country, Inventory
from sqlalchemy import select, update
from typing import List, Dict, Any, Optional
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from uuid import UUID


@connection
async def set_user(session, tg_id: int, username: str, full_name: str) -> Optional[User]:
    try:
        user = await session.scalar(select(User).filter_by(id=tg_id))

        if not user:
            new_user = User(id=tg_id, username=username, full_name=full_name)
            session.add(new_user)
            await session.commit()
            logger.info(f"Зарегистрировал пользователя с ID {tg_id}!")
            return None
        else:
            logger.info(f"Пользователь с ID {tg_id} найден!")
            return user
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()



@connection
async def add_avatar(session, user_id: int, race_id: int,
                     country_id: int,
                ) -> Optional[Avatar]:
    try:
        user = await session.scalar(select(User).filter_by(id=user_id))
        if not user:
            logger.error(f"Пользователь с ID {user_id} не найден.")
            return None
        
        race = await session.scalar(select(Race).filter_by(id=race_id))
        if not race:
            logger.error(f"Раса с ID {user_id} не найдена.")
            return None
        
        country = await session.scalar(select(Country).filter_by(id=country_id))
        if not country:
            logger.error(f"Страна с ID {user_id} не найдена.")
            return None
        
        max_hp = 0
        magic_power = 0
        attack = 0
        defense = 0
        strength = 0
        agility = 0
        intelligence = 0
        crit_chance = 0
        crit_damage = 0

        new_stats = AvatarStats(
            current_hp=max_hp,
            max_hp=max_hp,
            current_magic_power=magic_power,
            max_magic_power=magic_power,
            attack=attack,
            defense=defense,
            strength=strength,
            agility=agility,
            intelligence=intelligence,
            crit_chance=crit_chance,
            crit_damage=crit_damage
        )

        session.add(new_stats)
        
        new_inventory = Inventory(
        )

        session.add(new_inventory)


        '''
        new_grimoire = Grimoire(
        )

        session.add(new_grimoire)
        '''

        await session.flush()
        new_avatar = Avatar(
            #user_id=user_id,
            nick="тест",
            race_id=race_id,
            country_id=country_id,
            stats_id=new_stats.id,
            inventory_id=new_inventory.id,
            ##grimoire_id=new_grimoire.id
        )

        session.add(new_avatar)
        await session.flush()
        await session.execute(update(User).where(User.id == user_id).values(avatar_id=new_avatar.id))
        await session.commit()
        logger.info(
            f"Аватар для пользователя с ID {user_id} успешно добавлен!")
        return new_avatar
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении аватара: {e}")
        await session.rollback()




@connection
async def get_races(session, page, items_per_page) -> List[Dict[str, Any]]:
    try:
        offset = (page - 1) * items_per_page
        result = await session.execute(select(Race).offset(offset).limit(items_per_page))
        races = result.scalars().all()
        count = (await session.execute(func.count(Race.id))).scalars().all()[0]
        if not races:
            logger.info(f"Расы не найдены.")
            return []

        races_list = [
            {
                'id': race.id,
                'name': race.name,
                'description': race.description,
                "count": count
            } for race in races
        ]
        return races_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении рас: {e}")
        return []
    


@connection
async def get_countries(session, page, items_per_page) -> List[Dict[str, Any]]:
    try:
        offset = (page - 1) * items_per_page
        result = await session.execute(select(Country).offset(offset).limit(items_per_page))
        countries = result.scalars().all()
        count = (await session.execute(func.count(Country.id))).scalars().all()[0]
        if not countries:
            logger.info(f"Страны не найдены.")
            return []

        country_list = [
            {
                'id': country.id,
                'name': country.name,
                'description': country.description,
                "count": count
            } for country in countries
        ]

        return country_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении стран: {e}")
        return []
    


@connection
async def get_a_by_id(session, note_id: UUID) -> Optional[Dict[str, Any]]:
    try:
        note = await session.get(Note, note_id)
        if not note:
            logger.info(f"Заметка с ID {note_id} не найдена.")
            return None

        return {
            'id': note.id,
            'content_type': note.content_type,
            'content_text': note.content_text,
            'file_id': note.file_id
        }
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении заметки: {e}")
        return None