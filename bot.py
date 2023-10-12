from aiohttp import web
from plugins import web_server
from pyrogram import Client
import sys
from datetime import datetime
from log import (
PORT, 
LOGGER,
API_HASH, 
API_ID, 
BOT_TOKEN
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="GMBbot",
            api_hash=API_HASH,
            api_id=API_ID,
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

