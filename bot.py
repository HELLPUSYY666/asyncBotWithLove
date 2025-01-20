import asyncio
import logging

import structlog
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_reader import get_config, BotConfig, LogConfig
from logs import get_structlog_config
from structlog.typing import FilteringBoundLogger

from dispatcher import dp
import handlers

