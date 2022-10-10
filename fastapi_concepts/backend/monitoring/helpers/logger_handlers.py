import os
import logging

from logging.handlers import RotatingFileHandler

"""Logger constants"""
MAX_BYTES = 10000000  # Maximum size for a log file
BACKUP_COUNT = 9  # Maximum number of old log files
ERROR_FILE = "error.log"
IS_ERROR_LOGGER = True
DEBUG_FILE = "debug.log"
IS_DEBUG_LOGGER = True
# LOGGER_FORMATTER = "%(asctime)s | [%(log_env)s:%(name)s] | %(levelname)s \
# | [%(relativepath)s:%(funcName)s:%(lineno)d] | %(message)s"
LOGGER_FORMATTER = "%(asctime)s — %(log_env)s:%(name)s — %(levelname)s \
 — %(relativepath)s:%(funcName)s:%(lineno)d — %(message)s"


def make_logs_directory():
    directory = "backend_logs"
    make_directory = os.path.join(os.getcwd(), 'monitoring', directory)
    try:
        os.makedirs(make_directory, exist_ok=True)
    except OSError as e:
        print(e)
    return make_directory
                                                                         

def get_debug_handler():
    path_to_debug_log = os.path.join(make_logs_directory(), DEBUG_FILE)
    debug_handler = RotatingFileHandler(
        path_to_debug_log,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT
        )
    debug_handler.setLevel(logging.DEBUG)
    apm_formatter = logging.Formatter(LOGGER_FORMATTER)
    debug_handler.setFormatter(apm_formatter)
    return debug_handler


def get_error_handler():
    path_to_debug_log = os.path.join(make_logs_directory(), ERROR_FILE)
    error_handler = RotatingFileHandler(
        path_to_debug_log,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT
        )
    error_handler.setLevel(logging.ERROR)
    apm_formatter = logging.Formatter(LOGGER_FORMATTER)
    error_handler.setFormatter(apm_formatter)
    return error_handler
