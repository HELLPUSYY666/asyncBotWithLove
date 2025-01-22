from enum import StrEnum, auto
from functools import lru_cache
from os import environ
from tomllib import load
from typing import Type, TypeVar

from pydantic import BaseModel, SecretStr, field_validator

