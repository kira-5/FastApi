"""Config for DB Connection"""
import configparser
import os
from config.settings import get_settings


settings = get_settings()


def environment_config():
    """Read value from envioronmrnt file"""
    CONFIG = configparser.RawConfigParser()
    ENV = settings.ENVIRONMENT
    config_file_path = f"{os.getcwd()}/config/environment.cfg"
    CONFIG.read(config_file_path)
    return ENV, CONFIG
