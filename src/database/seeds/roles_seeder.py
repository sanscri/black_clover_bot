import json
import os

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models import Role


async def seed_roles(session: AsyncSession):
    try:
        json_path = os.path.join(
            os.path.dirname(__file__), '..', '..', '..', 'assets', 'data', 'roles.json'
        )
        with open(json_path, 'r', encoding='utf-8') as file:
            roles_to_seed = json.load(file)
        print(roles_to_seed)
        for role_data in roles_to_seed:
            print(role_data)
            role_name = role_data.get('name')

            if not role_name:
                print("[-] Skipping invalid role data: missing 'name'.")
                continue

            existing_role_query = await session.execute(
                select(Role).where(Role.name == role_name)
            )
            existing_role = existing_role_query.scalars().first()

            if not existing_role:
                print(f"[+] Creating new role '{role_name}'.")
                new_role = Role(name=role_name)
                session.add(new_role)

        await session.commit()
        print('[+] Roles seeded or updated successfully.')
    except Exception as e:
        await session.rollback()
        print(f'[-] Error while seeding or updating roles: {e}')
        raise