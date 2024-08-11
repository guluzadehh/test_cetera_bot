import asyncio
import os
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)

TIMEOUT = int(os.getenv("TIMEOUT"))
print(TIMEOUT)


async def timeout_reply(message: Message):
    try:
        await asyncio.sleep(TIMEOUT)
        await message.answer("Вы забыли ответить")
    except asyncio.CancelledError:
        pass
