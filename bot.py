import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from aiogram.filters.command import Command
from dotenv import dotenv_values

config = dotenv_values(".env")
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config["TG_TOKEN"])
# Диспетчер
dp = Dispatcher()


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="help", description="Помощь"),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет!")


@dp.message(Command("help"))
async def start(message: types.Message):
    await message.answer("Ты молодец, у тебя все получится!")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
