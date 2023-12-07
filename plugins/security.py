from pyrogram import filters, Client
import os
from pyrogram.types import (
Message,
CallbackQuery,
ChatPermissions,
InlineKeyboardButton, 
InlineKeyboardMarkup
)
from pyrogram.enums import ChatMemberStatus
from config import GROUP
from bot import Bot as app
import asyncio
from HELPER import (
callback_filter,
handle_exception,
cmd,
gen_wlcm,
hearts
)
from HELPER.Database import (
present_user, 
add_user, 
add_ruser_msg,
get_user
)
SPIC = ["https://graph.org/file/3ad7a84ee06897b580ced.jpg"]
Ronvkeyar = InlineKeyboardMarkup([[InlineKeyboardButton(text="COMPLETE RULES & GUIDLINES", url="https://telegra.ph/Anime-Chat-English--UCO-06-17"),]])


SCAP = """
{} __Welcome!__ {} [`{}`] 
    {} Kindly read Group: /rules 
        {} Enjoy your stay."""
RA_SCAP = "\n\n**❗__{} Your media permissions have been temporarily restricted for security reasons.__** <blockquote>__you will get unrestricted within few weeks for details:__\n__click👉🏻__  /details</blockquote>"


MAGREE = """
{} **Welcome!** {} [{}] 
    {} **Thankyou for understanding.**
        {} **Abide by rules and enjoy your stay.**
<blockquote>Media restriction info:  /details </blockquote><blockquote>Channels connect to group:  /links </blockquote><blockquote>Read group regulations and guidelines:  /rules </blockquote><blockquote>If you have any questions or need admins assistance:  /report </blockquote>"""


@app.on_callback_query(callback_filter('SRinfo'))
async def Admaction_callback_5(app: Client, query: CallbackQuery):
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
        elif Data.startswith("CLOSE$"):
            ouid = Data.split("$")[-1]
            if int(ouid) != UID: return await query.answer("This Is Not For You!", show_alert=True)
            await Update.delete()
            await query.answer("Thanks For Understanding 🩷", show_alert=False)
        else:
            await Update.delete()
    except Exception: return await handle_exception(app)


@app.on_chat_member_updated(filters.chat(GROUP))
async def welcome_sec1(app: app, message: Message): 
    try:
        if message.old_chat_member: return
        if message.new_chat_member.status == ChatMemberStatus.BANNED: return
        member = message.new_chat_member.user
        if member:
            RESTRICTED = await message.chat.restrict_member(
                user_id=member.id,
                permissions=ChatPermissions(
                    can_send_messages=True,
                    can_invite_users=True,
                    can_send_polls=True,
                    can_add_web_page_previews=False,
                    can_send_other_messages=False,
                    can_send_media_messages=False,
                    can_change_info=False,
                    can_pin_messages=False,
                ),
            )
            Username = f"@{member.username}" if member.username else f"{member.mention}"
            invkeyar = Ronvkeyar
            X, Y, Z = hearts()
            wlcm_txt = SCAP.format(X, member.mention, member.id, Y, Z)
            if RESTRICTED:
                invkeyar = InlineKeyboardMarkup([[InlineKeyboardButton(text="Understood, I Agree ✅", callback_data=f"SRinfo:TCA${member.id}"),]])
                wlcm_txt += RA_SCAP.format(Username)
                await app.send_message(chat_id=-1001649033559,text=f"🔷 #TEMP_MUTE\n» user: {member.mention} [`{member.id}`]\n @{Username}\n»group: {message.chat.title}\n#id{member.id}")
                if not await present_user(member.id): await add_user(member.id)
            wlcm_pic = await gen_wlcm(app, member)
            await app.send_photo(
                chat_id=message.chat.id,
                photo=wlcm_pic,
                caption=wlcm_txt,
                reply_markup=invkeyar
            )
            os.remove(f"Base/PFPZ/pic{member.id}.jpg")
    except Exception: return await handle_exception(app)








SCAP_E2 = """
<u>𝗔𝗻𝗶𝗺𝗲 𝗖𝗵𝗮𝘁 𝗖𝗼𝗺𝗺𝘂𝗻𝗶𝘁𝘆 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗦𝘆𝘀𝘁𝗲𝗺</u>
__To ensure a safe and enjoyable environment for all members, we've implemented some security measures. Which involves temporarily restricting media permissions for newer members.__
**__This action is taken to prevent spammers and the sharing of inappropriate or harmful content in group.__**

To regain your media permissions:
<blockquote>You have to be part of group for atleast 30 Days.</blockquote>
<blockquote>You must be active and sent atleast 100 meaningful messages.</blockquote>

```python
This ensures that you understand our guidelines and actively contributing to our community.
'Once you meet these requirements, feel free to remind Admins, and we‘ll promptly unrestrict your media permissions. Thank you for your understanding and cooperation. If you have any questions or concerns, don’t hesitate to ask. Welcome to the group!'
```
"""

@app.on_message(cmd(["sr", "rs", "details"]) & filters.group & filters.chat(GROUP))
async def Stickersecmsg(app: app, message: Message):
    member = message.from_user
    MId = message.id
    if message.reply_to_message:
        member = message.reply_to_message.from_user
        MId = message.reply_to_message.id
    Username = f"@{member.username}" if member.username else f"{member.mention}"
    invkeyar = InlineKeyboardMarkup([[InlineKeyboardButton(text="Understood | Close ✅", callback_data=f"SRinfo:CLOSE${member.id}"),]])
    await app.send_photo(chat_id=message.chat.id,photo=SPIC[0],caption=f"👤 {Username} [`{member.id}`]\n{SCAP_E2}",reply_markup=invkeyar,reply_to_message_id=MId)

@app.on_message(cmd(["cm", "minfo"]) & filters.group & filters.chat(GROUP))
async def resusermsgcount(app: app, message: Message):
    try: 
        member = message.from_user
        if message.reply_to_message:
            member = message.reply_to_message.from_user
        M = None
        if await present_user(member.id):
            M = await get_user(member.id)
            if not M: return await message.reply("Not Restricted By Me ツ")
        Username = f"@{member.username}" if member.username else f"{member.mention}"
        invkeyar = InlineKeyboardMarkup([[InlineKeyboardButton(text="»ᴄʟᴏꜱᴇ«", callback_data=f"SRinfo:CLOSE${member.id}"),]])
        await app.send_photo(chat_id=message.chat.id,photo="https://telegra.ph/file/69e674055f9de65d40b7b.jpg",caption=f"👤 {Username} [`{member.id}`]\n💬 Message Count: {M}",reply_markup=invkeyar,)
    except Exception: return await handle_exception(app)
