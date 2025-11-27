import asyncio
from create_bot import bot, dp, admins
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats, BotCommandScopeUnion

from handlers.start_router import start_router
from handlers.grimoire_router import grimoire_router
from handlers.battle_router import battle_router
from handlers.map.map_router import map_router
from handlers.dungeon.dungeon_router import dungeon_router
from handlers.profile_router import profile_router
from handlers.help_router import help_router

# Функция, которая настроит командное меню (дефолтное для всех пользователей)
async def set_commands():
    private_commands = [BotCommand(command='start', description='Старт'),
                    BotCommand(command='profile', description='Профиль'),
                    BotCommand(command='grimoire', description='Ваш гримуар'),
                    BotCommand(command='inventory', description='Ваш инвентарь'),
                    BotCommand(command='devils', description='Список всех дьяволов'),
                    BotCommand(command='spirits', description='Список всех духов'),
                    BotCommand(command='locations', description='Локации'),
                    BotCommand(command='daily', description='Ежедневки'),
                    BotCommand(command='quests', description='Квесты'),
                    BotCommand(command='achiv', description='Достижения'),
                    BotCommand(command='stats', description='Статистика'),
                    BotCommand(command='map', description='Карта'),
                    BotCommand(command='help', description='Помощь')]
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='help', description='Помощь')]
    await bot.set_my_commands(private_commands, BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands, BotCommandScopeAllGroupChats())


# Функция, которая выполнится когда бот запустится
async def start_bot():
    await set_commands()
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, f'Я запущен🥳.')
        except:
            pass


# Функция, которая выполнится когда бот завершит свою работу
async def stop_bot():
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, 'Бот остановлен. За что?😔')
    except:
        pass


async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(dungeon_router)
    dp.include_router(map_router)
    dp.include_router(battle_router)
    dp.include_router(grimoire_router)
    dp.include_router(profile_router)
    dp.include_router(help_router)
    # регистрация функций
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # запуск бота в режиме long polling при запуске бот очищает все обновления, которые были за его моменты бездействия
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())


