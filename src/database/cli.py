# cli.py
import asyncio

import typer

from database.seeds.roles_seeder import seed_roles
from settings import settings
from database.database import async_session
cli = typer.Typer()


async def run_seed(func):
    async_session.init(settings.get_db_url)
  
    async with async_session.session() as session:
        await func(session)
        await session.commit()
    await async_session .close()


@cli.command()
def roles():
    asyncio.run(run_seed(seed_roles))


@cli.command()
def categories():
    asyncio.run(run_seed(seed_categories))


@cli.command()
def articles():
    asyncio.run(run_seed(seed_articles))


if __name__ == '__main__':
    cli()