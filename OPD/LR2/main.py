from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
import asyncio
import random
import logging

API_TOKEN = "7949826200:AAHEkia1CLL8USTVPO4j97IAsXvqZFFapQE"  

logging.basicConfig(level=logging.INFO)


user_data = {}

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


play_again_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/start")]],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    user_data[user_id] = {
        "number": random.randint(1, 100),
        "attempts": 0
    }
    await message.answer(
        "🎯 Я загадал число от 1 до 100. Попробуй угадать!",
        reply_markup=types.ReplyKeyboardRemove()
    )

@dp.message()
async def handle_guess(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()

    if user_id not in user_data:
        await message.answer("Пожалуйста, начни игру с команды /start.")
        return

    if not text.isdigit():
        await message.answer("❗ Введи число от 1 до 100.")
        return

    guess = int(text)
    game = user_data[user_id]
    game["attempts"] += 1
    target = game["number"]
    attempts = game["attempts"]

    if guess < target:
        await message.answer(f"Попытка №{attempts}: Моё число больше ⬆️")
    elif guess > target:
        await message.answer(f"Попытка №{attempts}: Моё число меньше ⬇️")
    else:
        await message.answer(
            f"🎉 Угадал! Моё число было <b>{target}</b>.\n"
            f"Ты справился за <b>{attempts}</b> попыток!",
            reply_markup=play_again_keyboard
        )
        del user_data[user_id]


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
