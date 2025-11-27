# roles_seeder.py
import json
import os

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models import Race


async def seed_races(session: AsyncSession):
    try:
        json_path = os.path.join(
            os.path.dirname(__file__), '..', '..', '..', 'assets', 'data', 'races.json'
        )
        with open(json_path, 'r', encoding='utf-8') as file:
            races_to_seed = json.load(file)

        for race_data in races_to_seed:
            race_name = race_data.get('name')
            race_description = race_data.get('description')
            if not race_name:
                print("[-] Skipping invalid race data: missing 'race'.")
                continue

            existing_race_query = await session.execute(
                select(Race).where(Race.name == race_name)
            )
            existing_role = existing_race_query.scalars().first()

            if not existing_role:
                print(f"[+] Creating new role '{race_name}'.")
                new_race = Race(name=race_name, description=race_description)
                session.add(new_race)

        await session.commit()
        print('[+] Races seeded or updated successfully.')
    except Exception as e:
        await session.rollback()
        print(f'[-] Error while seeding or updating races: {e}')
        raise