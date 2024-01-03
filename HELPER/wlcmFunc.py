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
    'Base/WP12.jpg'
]
STK_IMG = ['Base/STK/S01.png', 'Base/STK/S02.png', 'Base/STK/S03.png', 'Base/STK/S04.png', 'Base/STK/S05.png', 'Base/STK/S06.png', 'Base/STK/S07.png', 'Base/STK/S08.png', 'Base/STK/S09.png', 'Base/STK/S10.png', 'Base/STK/S11.png', 'Base/STK/S12.png', 'Base/STK/S13.png', 'Base/STK/S14.png', 'Base/STK/S15.png', 'Base/STK/S16.png', 'Base/STK/S17.png', 'Base/STK/S18.png', 'Base/STK/S19.png', 'Base/STK/S20.png', 'Base/STK/S21.png', 'Base/STK/S22.png', 'Base/STK/S23.png', 'Base/STK/S24.png', 'Base/STK/S25.png', 'Base/STK/S26.png', 'Base/STK/S27.png', 'Base/STK/S28.png', 'Base/STK/S29.png', 'Base/STK/S30.png', 'Base/STK/S31.png', 'Base/STK/S32.png', 'Base/STK/S33.png', 'Base/STK/S34.png', 'Base/STK/S35.png', 'Base/STK/S36.png', 'Base/STK/S37.png', 'Base/STK/S38.png', 'Base/STK/S39.png', 'Base/STK/S40.png']

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
