import asyncio
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, F
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
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Создать сетку",
        callback_data="grid")
    )
    await message.answer("Привет! Ты зашел в бота rc tournaments 4all, что ты хочешь от нас?",
         reply_markup=builder.as_markup()                 
    )

@dp.callback_query(F.data == "grid")
async def send_grid(callback: types.CallbackQuery):
    await callback.message.answer(text="Введите имена пилотов одним сообщением.")
    await callback.answer()
    

@dp.message(Command("help"))
async def start(message: types.Message):
    await message.answer("Ты молодец, у тебя все получится!")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
