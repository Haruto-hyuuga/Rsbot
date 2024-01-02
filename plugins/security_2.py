from pyrogram import filters, Client
import os
from pyrogram.types import (
Message,
InlineKeyboardButton, 
InlineKeyboardMarkup
)
from pyrogram.enums import ChatMemberStatus
from bot import Bot as app
from HELPER import (
handle_exception,
gen_wlcm,
hearts,
)
Ronvkeyar = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="COMPLETE RULES & GUIDLINES", url="https://telegra.ph/Anime-Chat-English--UCO-06-17"),
        ]
    ]
)

SCAP = """
{} __Welcome!__ {} [`{}`] 
    {} **Kindly read Group:** /rules 
        {} **Enjoy your stay.**"""


@app.on_chat_member_updated(filters.chat(-1002110733388))
async def hnwelcome_msg2(app: app, message: Message):
    try:
        member = message.new_chat_member.user
        if message.old_chat_member:
            if message.from_user.id != message.old_chat_member.user.id: return
            if message.new_chat_member.is_member is False: return 
            if message.old_chat_member.status in [ChatMemberStatus.RESTRICTED, ChatMemberStatus.LEFT]:
                wlcm_pic = await gen_wlcm(app, member)
                X, Y, Z = hearts()
                Left = "<blockquote>If you left group before due to media restrictions, please be aware that the restrictions remain unchanged</blockquote>"
                await app.send_photo(chat_id=message.chat.id,photo=wlcm_pic,caption=f"{SCAP.format(X, member.mention, member.id, Y, Z)}\n\n{Left}")
                os.remove(wlcm_pic)
            return
        if message.new_chat_member.status == ChatMemberStatus.BANNED: return
        if member:
            Username = f"@{member.username}" if member.username else f"{member.mention}"
            X, Y, Z = hearts()
            wlcm_txt = SCAP.format(X, member.mention, member.id, Y, Z)
            wlcm_pic = await gen_wlcm(app, member)
            if message.from_user.id != member.id:
                addder = f"@{message.from_user.username}" if message.from_user.username else f"{message.from_user.mention}"
                wlcm_txt += f"\n<blockquote>🫂 Thanks {addder} for inviting {Username}</blockquote>"
            await app.send_photo(
                chat_id=message.chat.id,
                photo=wlcm_pic,
                caption=wlcm_txt,
                reply_markup=Ronvkeyar
            )
            os.remove(wlcm_pic)
    except Exception:
        FileN = f"Error_{message.id}.json"
        with open(FileN, "w+", encoding="utf8") as out_file:
            out_file.write(str(message))       
        await app.send_document(5329765587, document=FileN)
        os.remove(FileN)
        return await handle_exception(app)



