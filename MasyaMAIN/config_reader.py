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
