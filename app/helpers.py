import asyncio
import os
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TIMEOUT = int(os.getenv("TIMEOUT"))


async def timeout_reply(message: Message):
    try:
        await asyncio.sleep(TIMEOUT)
        await message.answer("Вы забыли ответить")
    except asyncio.CancelledError:
        pass
