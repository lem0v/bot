from aiogram import Bot, Dispatcher, types
import asyncio


bot = Bot("6479684117:AAHxii-KdU9lm6RlS8GW1OuDJ7AQyTFdwW0")
dp = Dispatcher()

@dp.message()
async def start_command(message: types.Message):
    if message.text == "/start":
        await message.answer(text="Добро пожаловать в казино Рояяль!")
        await message.delete()
    elif message.text == "/help":
        await message.answer("lol")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())