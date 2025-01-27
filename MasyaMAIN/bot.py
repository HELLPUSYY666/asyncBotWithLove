import asyncio
import logging

import structlog
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_reader import *
from logs import get_structlog_config


async def main():
    log_config: LogConfig = get_config(model=LogConfig, root_key='logs')
    structlog.configure(**get_structlog_config(log_config))

    bot_config: BotConfig = get_config(model=BotConfig, root_key="bot")

    bot = Bot(
        token=bot_config.token.get_secret_value(),  # get token as secret, so it will be hidden in logs
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML  # ParseMode (HTML or MARKDOWN_V2 is preferable)
        )
    )


