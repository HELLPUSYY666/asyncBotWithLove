import asyncio
import logging

import structlog
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_reader import LogConfig, get_config
from logs import get_structlog_config


async def main():
    log_config: LogConfig = get_config(model=LogConfig, root_key='logs')
    structlog.configure(**get_structlog_config(log_config))

