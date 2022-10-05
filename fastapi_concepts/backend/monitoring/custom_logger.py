import logging
import uvicorn
from logging.config import dictConfig
from monitoring.helpers.logger_filters import EnvPathFilter, PackagePathFilter
from monitoring.helpers.logger_adapter import LoggerAdapter
from monitoring.helpers.logger_handlers import get_debug_handler, \
    get_error_handler

IS_DEBUG_LOGGER = True
IS_ERROR_LOGGER = True


def configure_logging():
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    # log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    return log_config


def get_logger(module_name, log_name=None, msg=None):  # type: ignore
    log_config = configure_logging()
    dictConfig(log_config)
    if module_name:
        logger = logging.getLogger(log_name) \
            if log_name else logging.getLogger(module_name)

        api_logger = logging.getLogger("uvicorn.access")
        loggers = [logger, api_logger]
        for logger_ in loggers:
            logger_.setLevel(logging.INFO)
            logger_.addFilter(EnvPathFilter())
            logger_.addFilter(PackagePathFilter())
            if IS_DEBUG_LOGGER:
                logger.addHandler(get_debug_handler())
            # if IS_ERROR_LOGGER:
            #     logger.addHandler(get_error_handler())
        logger_extra_msg = msg or '-'
        logger = LoggerAdapter(logger, logger_extra_msg)

        return logger
