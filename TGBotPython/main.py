 from aiogram import Bot, Dispatcher, F
import asyncio
from app.handlers import router



async def main():
    bot = Bot(token='7629041019:AAESPtXMz6UCdeT3tSbtAiyfXW_zyJ1gyPI')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())