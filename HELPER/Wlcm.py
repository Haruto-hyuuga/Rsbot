from random import choice
from PIL import Image, ImageDraw
BASE_IMG = [
    'Base/WP01',
    'Base/WP02',
    'Base/WP03', 
    'Base/WP04',
    'Base/WP05', 
    'Base/WP06',
    'Base/WP07',
    'Base/WP08', 
    'Base/WP09', 
    'Base/WP10', 
    'Base/WP11', 
    'Base/WP12'
]
STK_IMG = [
    'Base/STK'
]
async def gen_wlcm(app, member):
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
    
    draw = ImageDraw.Draw(i1)
    draw.text((0,0), f" @AnimeChatCommunity\n{message.date} | [{member.id}]", fill="black", stroke_width=6, stroke_fill="white")
    i1.save(f"downloads/pic1.jpg")
