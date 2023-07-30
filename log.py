import os

API_ID = 12621397
API_HASH = "e68f9fdc9c8e562d9dab37ac3731a7b6"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PORT = os.environ.get("PORT", "8080")

import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "AnimeRobots.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
