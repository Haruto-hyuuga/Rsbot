from pyrogram import filters
from typing import Union
from config import botusername

def cmd(comm: Union[list, str]):
  res = list()
  if isinstance(comm, str):
    res.extend([comm, f"{comm}@{botusername}"])
  if isinstance(comm, list):
    for com in comm:
      res.extend([com, f"{com}@{botusername}"])
  return filters.command(res, prefixes=["/", "?", "$", "!", "#", "@", ",", ".", "+", "~", "™", ";", ":", "-", "_"]) 

def parse_com(com, key):
  try:
    r = com.split(key,1)[1]
  except KeyError:
    return None
  r = (r.split(" ", 1)[1] if len(r.split()) >= 1 else None)
  return r


def callback_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )

import traceback
import sys 
async def handle_exception(Bot):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    tb_info = traceback.extract_tb(exc_traceback)
    filename, line_num, func_name, code = tb_info[-1]

    error_message = f"⚠️ 𝗘𝗥𝗥𝗢𝗥:\n\n"
    error_message += f"ᴄᴏᴅᴇ: **{code}**\n"
    error_message += f"ꜰɪʟᴇ: **{filename}**\n"
    error_message += f"ʟɪɴᴇ: **{line_num}**\n"
    error_message += f"ꜰᴜɴᴄᴛɪᴏɴ: **{func_name}**\n"
    error_message += f"ᴇʀʀᴏʀ: **{exc_value}**\n"
    await Bot.send_message(5329765587, error_message)

def system_reboot(UID): 
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)



from pyrogram.types import Sticker
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
async def get_stickers(app, short_name):
    sticker_set = await app.invoke(
        GetStickerSet(stickerset=InputStickerSetShortName(short_name=short_name), hash=0)
    )
    
    sticker_list = []

    for doc in sticker_set.documents:
        try:
            sticker = await Sticker._parse(app, doc, {type(a): a for a in doc.attributes})
            if sticker.file_size > 0:
                sticker_list.append(sticker)
        except Exception as e:
            print(f"Error parsing sticker: {e}")

    return sticker_list


from pyrogram import raw
from  pyrogram.utils import parse_text_entities

async def InvertMD_edit(bot, chat_id, msg_id):
    Peer = await bot.resolve_peer(chat_id)
    X = await bot.get_messages(chat_id, msg_id)
    Newmsg = X.text.html
    await bot.invoke(raw.functions.messages.EditMessage(
        peer=Peer,
        id=msg_id,
        **await parse_text_entities(bot, Newmsg, None, None),
        reply_markup=await X.reply_markup.write(bot),
        invert_media=True
    ))
