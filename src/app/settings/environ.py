"""
Define env object and read .env file
"""
import os.path

import environ  # type: ignore

from . import BASE_DIR

env = environ.Env(
    DEBUG=(bool, False),
    # CI=(bool, False),
)

env_path = BASE_DIR / ".env"

if os.path.exists(env_path):
    environ.Env.read_env(env_path)  # reading .env file

DEBUG = env("DEBUG", cast=bool, default=False)

__all__ = [
    "env",
]
