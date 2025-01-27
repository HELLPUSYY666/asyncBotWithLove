from enum import StrEnum, auto
from functools import lru_cache
from os import environ
from tomllib import load
from typing import Type, TypeVar

from pydantic import BaseModel, SecretStr, field_validator

ConfigType = TypeVar("ConfigType", bound=BaseModel)


class LogRenderer(StrEnum):
    JSON = auto()
    CONSOLE = auto()


class BotConfig(BaseModel):
    token: SecretStr
    owners: list


class LogConfig(BaseModel):
    show_datetime: bool
    datetime_format: str
    show_debug_logs: bool
    time_in_utc: bool
    use_colors_in_console: bool
    renderer: LogRenderer


    @field_validator("renderer", mode='before')
    @classmethod
    def log_renderer_to_lower(cls, v: str):
        return v.lower()

class Config(BaseModel):
    bot: BotConfig
