from aiohttp import web
from plugins import web_server
from pyrogram import Client
import sys
from datetime import datetime
LOG_FILE_NAME = "AnimeRobots.txt"
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PORT = os.environ.get("PORT", "8080")
import logging
from logging.handlers import RotatingFileHandler
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

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="GMBbot",
            api_hash="95d8b38bbb62d087dbf7b98abf670e78",
            api_id=9855603,
            plugins={
                "root": "plugins"
            },
            workers=30,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.username = bot_me.username
        self.id = bot_me.id


        self.LOGGER(__name__).info(f"{bot_me.first_name} IS ONLINE! ✅\n Client ID: {bot_me.id} ⚡")
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. 🔥")

