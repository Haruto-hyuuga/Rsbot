import time
import math
from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from datetime import datetime

def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

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

@Bot.on_message(filters.command(['uptime', 'ping']))
async def stats(bot: Bot, message: Message):
    start_time = time.time()
    P_MSG = await bot.send_photo(message.chat.id, photo="https://telegra.ph/file/3932401941f0bda36dd64.jpg")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    
    now = datetime.now()
    delta = now - bot.uptime
    uptime = get_readable_time(delta.seconds)
    
    start_processing = time.time()
    primes = generate_primes(100000)
    end_processing = time.time()
    process_time = round(end_processing - start_processing, 3)
    
    await P_MSG.edit(f"""
__⚡ PING:__    **{ping_time} milliseconds**

__🌍 UPTIME:__    **{uptime}**

__⏱️ PROCESSING SPEED:__    **{process_time} seconds**

__📡 HOSTED BY:__ @ANIMEROBOTS 
"""
    )
