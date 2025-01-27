import structlog
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_reader import *
from logs import get_structlog_config
from structlog.typing import FilteringBoundLogger
from MasyaMAIN.dispatcher import dp


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

    logger: FilteringBoundLogger = structlog.get_logger()
    await logger.ainfo("Starting the bot...")

    try:
        await dp.start_polling(bot,
                               skip_updates=False)  # Don't skip updates, if your bot will process payments or other important stuff
    finally:
        await bot.session.close()



