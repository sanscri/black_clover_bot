# cli.py
import asyncio

import typer

from database.seeds.roles_seeder import seed_roles
from database.seeds.races_seeder import seed_races
from database.seeds.map_seeder import seed_map
from database.base import connection
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

@cli.command()
def map():
    asyncio.run(run_seed(seed_map))

if __name__ == '__main__':
    cli()