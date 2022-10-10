
# import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

ENVIRONMENT = None


class Settings():
    # environment = os.getenv("env")
    ENVIRONMENT = 'local'

    class config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
