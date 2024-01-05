import os
from random import choice, sample
from PIL import Image
ERR_IMG = "https://telegra.ph/file/2de95979a8b2b56ce6937.jpg"
from HELPER import handle_exception

BASE_IMG = [
    'Base/WP01.jpg',
    'Base/WP02.jpg',
    'Base/WP03.jpg', 
    'Base/WP04.jpg',
    'Base/WP05.jpg', 
    'Base/WP06.jpg',
    'Base/WP07.jpg',
    'Base/WP08.jpg', 
    'Base/WP09.jpg', 
    'Base/WP10.jpg', 
    'Base/WP11.jpg', 
    'Base/WP12.jpg',
    'Base/WP13.jpg', 
    'Base/WP14.jpg',
    'Base/WP15.jpg',
    'Base/WP16.jpg',
]
STK_IMG = []
directory_path = 'Base/STK'
files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
STK_IMG.extend(files)


async def gen_wlcm(app, member):
    try:
        i1 = Image.open(choice(BASE_IMG))
        try:
            user_pic = await app.download_media(member.photo.big_file_id, f"Base/PFPZ/{member.id}.jpg")
        except:
            user_pic = "Base/PFPZ/WPnone.jpg"
        PFP = Image.open(user_pic)
        PFP = PFP.resize((320,320))
        i1.paste(PFP, (355,255))
    
        STK = Image.open(choice(STK_IMG))
        STK = STK.resize((450,450))
        i1.paste(STK, (-20,270), mask=STK)
        
        i1.save(f"Base/PFPZ/pic{member.id}.jpg")
        return f"Base/PFPZ/pic{member.id}.jpg"
    except Exception:
        await handle_exception(app)
        return ERR_IMG
    finally:
        try: os.remove(f"Base/PFPZ/{member.id}.jpg")
        except: pass



hearts_emojis_1 = ['❤️', '🧡', '💛', '💚', '💙', '💜', '🤍', '🩷', '🩵', '🩶', '🖤', '♥️', '💖', '💝', '❤️‍🩹']
hearts_emojis_2 = ['💖', '💕', '💞', '💓', '💗', '💝', '💘', '❤️‍🔥', '❤️‍🩹', '💟']

def hearts():
    Hearts = hearts_emojis_1 #choice([hearts_emojis_1, hearts_emojis_1, hearts_emojis_2, hearts_emojis_1, hearts_emojis_1])
    X, Y, Z = sample(Hearts, 3)
    return X, Y, Z

import aiohttp
Errpic = "https://telegra.ph/file/96fa9f03a0e860d4c6b4b.jpg"
async def get_anime_banner():
    try:
        url = "https://nekos.best/api/v2/waifu"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return Errpic
                data = await response.json()
            image = data['results'][0]['url']
            if image is None: 
                return Errpic
            return image
    except: return Errpic
