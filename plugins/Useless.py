import time
from bot import Bot
from pyrogram.types import Message, InputMediaPhoto
from pyrogram import filters
from datetime import datetime
import platform
from sys import version as pyver
import psutil
from pyrogram import __version__ as pyrover
from config import ADMINS 

async def stats_global():
    sc = platform.system()
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}MHz"
    except:
        cpu_freq = "Unable to Fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    
    text = f"""
<blockquote>📟 𝙃𝘼𝙍𝘿𝙒𝘼𝙍𝙀</blockquote>
  > ᴩʟᴀᴛғᴏʀᴍ: **{sc}**
  > ʀᴀᴍ: **{ram}**
  > ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs: **{p_core}**
  > ᴛᴏᴛᴀʟ ᴄᴏʀᴇs: **{t_core}**
  > ᴄᴩᴜ ғʀᴇǫᴜᴇɴᴄʏ: **{cpu_freq}**
  
<blockquote>💾 𝙎𝙏𝙊𝙍𝘼𝙂𝙀</blockquote>
  > ᴀᴠᴀɪʟᴀʙʟᴇ: **{total[:4]} GiB**
  > ᴜsᴇᴅ: **{used[:4]} GiB**
  > ғʀᴇᴇ: **{free[:4]} GiB**

<blockquote>💻 SOFTWARE</blockquote>
  > ᴩʏᴛʜᴏɴ: **{pyver.split()[0]}**
  > ᴩʏʀᴏɢʀᴀᴍ: **{pyrover}**
"""
    return text



def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "min", "hr", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time

@Bot.on_message(filters.command(['uptime', 'ping', 'stats']) & filters.user(ADMINS))
async def Uptime_Ping_1(bot: Bot, message: Message):
    start_time = time.time()
    P_MSG = await bot.send_photo(message.chat.id, photo="https://telegra.ph/file/3932401941f0bda36dd64.jpg")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    
    now = datetime.now()
    delta = now - bot.uptime
    uptime = get_readable_time(delta.seconds)
    sys_stats = await stats_global()
    await P_MSG.edit(f"""{sys_stats}
__⚡ PING:__    **{ping_time} milliseconds**
__🌍 UPTIME:__    **{uptime}** 
"""
    )


import asyncio
import speedtest

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("ᴄʜᴇᴄᴋɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ...")
        test.download()
        m = m.edit("ᴄʜᴇᴄᴋɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("ᴜᴩʟᴏᴀᴅɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...")
    except Exception as e:
        return m.edit(e)
    return result

@Bot.on_message(filters.command(["speedtest", "spd"]) & filters.user(ADMINS))
async def speedtest_function(bot: Bot, message: Message):
    m = await message.reply_animation(
        animation="https://telegra.ph/file/2295b1f4737321f294e31.mp4",
        caption="Running Speed Test"
    )
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴩ:__** {result['client']['isp']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ:**</u>
**__ɴᴀᴍᴇ:__** {result['server']['name']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__sᴩᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__ᴩɪɴɢ:__** {result['ping']}"""
    Medit = InputMediaPhoto(media=result["share"], caption=output)
    await m.edit_media(Medit)
    



