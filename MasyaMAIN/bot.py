import asyncio
import logging

import structlog
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


async def main():
    log_config: LogConif = get_config(model=LogConfig, root_key='logs')
