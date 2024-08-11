import asyncio
from aiogram.dispatcher.router import Router
from aiogram.fsm.state import State
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from .helpers import timeout_reply

router = Router()

wait_for_res = State()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(wait_for_res)
    await message.answer(f"Привет, {message.from_user.username}! Как ты сегодня?")

    timer = asyncio.create_task(timeout_reply(message))
    await state.update_data(timer=timer)


@router.message(wait_for_res)
async def process_input(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    timer: asyncio.Task = data.get("timer")
    if timer:
        timer.cancel()

    await state.clear()
