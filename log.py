import os

API_ID = 9855603
API_HASH = "95d8b38bbb62d087dbf7b98abf670e78"
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
