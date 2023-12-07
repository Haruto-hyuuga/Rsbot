from pyrogram import filters, Client
from pyrogram.types import Message
from bot import Bot as bot
from config import GROUP
from HELPER import handle_exception
from HELPER.Database import (
present_user, 
add_ruser_msg,
get_user,
del_user
)


@bot.on_message(filters.chat(GROUP) & filters.group & filters.text, group=5)
async def mgc_allmsg(bot: bot, message: Message):
    try:
        user = message.from_user
        if message.text:
            if await present_user(user.id):
                if len(message.text) >= 50:
                    await add_ruser_msg(user.id)
                Msgs = await get_user(user.id)
                if int(Msgs) >= 100:
                    await message.chat.unban_member(user.id)
                    await del_user(user.id)
                    await message.reply(f"👤 {user.mention} [`{user.id}`] completed 100 messages!\nYou can now send stickers and media.")
    except Exception: return await handle_exception(bot)
