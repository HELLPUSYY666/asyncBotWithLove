import structlog
from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from fluent.runtime import FluentLocalization

router = Router()
router.message.filter(F.chat.type == "group")

logger = structlog.get_logger()


@router.message(F.content_type.in_({'new_chat_members', 'left_chat_member'}))
async def on_user_join_or_left(message: Message):
    await message.delete()
