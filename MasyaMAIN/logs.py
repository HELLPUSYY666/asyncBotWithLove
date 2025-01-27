import logging
from json import dumps

import structlog
from structlog import WriteLoggerFactory

from config_reader import LogConfig, LogRenderer


def get_structlog_config(
        log_config: LogConfig
) -> dict:
    if log_config.show_debug_logs is True:
        min_level = logging.DEBUG
    else:
        min_level = logging.INFO

    return {
        "processors": get_processors(log_config),
        "cache_logger_on_first_use": True,
        "wrapper_class": structlog.make_filtering_bound_logger(min_level),
        "logger_factory": WriteLoggerFactory()
    }


def get_processors(log_config: LogConfig) -> list:
    def custom_json_serializer(data, *args, **kwargs):
        result = dict()

        if log_config.show_datetime is True:
            result["timestamp"] = data.pop("timestamp")

        for key in ("level", "event"):
            if key in data:
                result[key] = data.pop(key)

        result.update(**data)
        return dumps(result, default=str)

    processors = list()

    if log_config.show_datetime is True:
        processors.append(structlog.processors.TimeStamper(
            fmt=log_config.datetime_format,
            utc=log_config.time_in_utc
        )
        )

    processors.append(structlog.processors.add_log_level)

    if log_config.renderer == LogRenderer.JSON:
        processors.append(structlog.processors.JSONRenderer(serializer=custom_json_serializer))
    else:
        processors.append(structlog.dev.ConsoleRenderer(
            # You can turn off colors in the logs
            colors=log_config.use_colors_in_console,
            # You can remove padding in levels, i.e. instead of
            # [info   ] Some info log
            # [warning] Some warning log
            # will be
            # [info] Some info log
            # [warning] Some warning log
            pad_level=True
        ))
    return processors
