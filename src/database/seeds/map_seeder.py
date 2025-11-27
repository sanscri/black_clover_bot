import json
import os

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models import Country


async def seed_map(session: AsyncSession):
    try:
        json_path = os.path.join(
            os.path.dirname(__file__), '..', '..', '..', 'assets', 'data', 'map', 'map.json'
        )
        with open(json_path, 'r', encoding='utf-8') as file:
            map_to_seed = json.load(file)

        for map_data in map_to_seed:
            country_name = map_data.get('name')
            country_full_name = map_data.get('fullName')
            country_description = map_data.get('description')
            country_symbol = map_data.get('symbol')
            if not country_name:
                print("[-] Skipping invalid race data: missing 'race'.")
                continue

            existing_race_query = await session.execute(
                select(Country).where(Country.name == country_name)
            )
            existing_country = existing_race_query.scalars().first()

            if not existing_country:
                print(f"[+] Creating new role '{country_name}'.")
                new_country = Country(name=country_name, 
                                    full_name=country_full_name,
                                    description=country_description, 
                                    symbol=country_symbol)
                session.add(new_country)

        await session.commit()
        print('[+] Races seeded or updated successfully.')
    except Exception as e:
        await session.rollback()
        print(f'[-] Error while seeding or updating races: {e}')
        raise