from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import structlog
import MasyaMAIN.keyboards.confirm

router = Router()
router.message.filter(F.chat.type == "private")
logger = structlog.get_logger()


@router.message(CommandStart())
async def start_func(message: Message):
    await message.reply(
        f"Привет! Кажется ты масик и твой ID: {message.from_user.id}\nТвое масюлистое имя: {message.from_user.first_name}")
