# cli.py
import asyncio

import typer

from database.seeds.roles_seeder import seed_roles
from database.seeds.races_seeder import seed_races
from settings import settings
from database.base import connection
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
cli = typer.Typer()


@connection
async def run_seed(session, func):
    await func(session)
    await session.commit()


@cli.command()
def roles():
    asyncio.run(run_seed(seed_roles))


@cli.command()
def races():
    asyncio.run(run_seed(seed_races))



if __name__ == '__main__':
    cli()