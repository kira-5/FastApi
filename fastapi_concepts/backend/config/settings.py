import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()


class Settings():
    environment = os.getenv("env")

    class config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
