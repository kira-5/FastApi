import logging
import os
import sys

from config.settings import get_settings

settings = get_settings()


class EnvPathFilter(logging.Filter):
    def filter(self, record):
        record.log_env = f"{settings.environment}-script"
        return True


class PackagePathFilter(logging.Filter):
    def filter(self, record):
        pathname = record.pathname
        record.relativepath = None
        abs_sys_paths = map(os.path.abspath, sys.path)
        for path in sorted(
            abs_sys_paths,
            key=len,
            reverse=True
        ):  # longer paths first
            if not path.endswith(os.sep):
                path += os.sep
            if pathname.startswith(path):
                record.relativepath = os.path.relpath(pathname, path)
                break
        return True
