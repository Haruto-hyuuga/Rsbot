from pyrogram import filters, Client
from pyrogram.types import Message
from bot import Bot as bot
from config import GROUP
from HELPER import handle_exception
from HELPER.Database import (
present_user, 
add_ruser_msg,
)


@bot.on_message(filters.chat(GROUP) & filters.group, group=5)
async def mgc_allmsg(bot: bot, message: Message):
    try:
        user = message.from_user
        if message.text:
            if await present_user(user.id):
                if len(message.text) >= 70:
                    await add_ruser_msg(user.id)
    except Exception:
        await handle_exception(bot)
