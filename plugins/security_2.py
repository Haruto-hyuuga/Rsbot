from pyrogram import filters, Client
import os
from pyrogram.types import (
Message,
CallbackQuery,
InlineKeyboardButton, 
InlineKeyboardMarkup
)
from pyrogram.enums import ChatMemberStatus
from config import ADMINS
from bot import Bot as app
import asyncio
from HELPER import (
callback_filter,
handle_exception,
gen_wlcm,
hearts,
)
Ronvkeyar = InlineKeyboardMarkup([[InlineKeyboardButton(text="COMPLETE RULES & GUIDLINES", url="https://telegra.ph/Anime-Chat-English--UCO-06-17"),]])


SCAP = """
{} __Welcome!__ {} [`{}`] 
    {} **Kindly read Group:** /rules 
        {} **Enjoy your stay.**"""


@app.on_callback_query(callback_filter('S2wclm'))
async def hnwelcm_callback_5(app: Client, query: CallbackQuery):
    Data = query.data.split(":")[1]
    Update = query.message
    UID = query.from_user.id
    try:
        if Data.startswith("TCA$"):
            ouid = Data.split("$")[-1]
            if int(ouid) != UID:
                return await query.answer("This Is Not For You, Let The New Member Agree To Terms & Condition", show_alert=True)
            X, Y, Z = hearts()
            await Update.edit(
                MAGREE.format(X, query.from_user.mention, ouid, Y, Z),
                reply_markup=Ronvkeyar
            )
            await query.answer("Type Command: /details or /rs\nTo get detailed info how to media permission", show_alert=True)
        elif Data.startswith("CLOSE$"):
            ouid = Data.split("$")[-1]
            if int(ouid) != UID: return await query.answer("This Is Not For You!", show_alert=True)
            await Update.delete()
            await query.answer("Thanks For Understanding 🩷", show_alert=False)
        else:
            await Update.delete()
    except Exception: return await handle_exception(app)


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
            invkeyar = Ronvkeyar
            X, Y, Z = hearts()
            wlcm_txt = SCAP.format(X, member.mention, member.id, Y, Z)
            await app.send_message(chat_id=-1001649033559,text=f"🔷 #TEMP_MUTE\n» user: {member.mention} [`{member.id}`]\n {Username}\n»group: {message.chat.title}\n#id{member.id}")
            wlcm_pic = await gen_wlcm(app, member)
            if message.from_user.id != member.id:
                addder = f"@{message.from_user.username}" if message.from_user.username else f"{message.from_user.mention}"
                wlcm_txt += f"\n<blockquote>🫂 Thanks {addder} for inviting {Username}</blockquote>"
            await app.send_photo(
                chat_id=message.chat.id,
                photo=wlcm_pic,
                caption=wlcm_txt,
                reply_markup=invkeyar
            )
            os.remove(wlcm_pic)
    except Exception:
        FileN = f"Error_{message.id}.json"
        with open(FileN, "w+", encoding="utf8") as out_file:
            out_file.write(str(message))       
        await app.send_document(5329765587, document=FileN)
        os.remove(FileN)
        return await handle_exception(app)



