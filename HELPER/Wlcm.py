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

async def gen_wlcm(app, member):
    i1 = Image.open(choice(BASE_IMG))
    try:
        user_pic = await app.download_media(member.photo.big_file_id, f"Base/PFPZ/{member.id}.jpg")
    except:
        user_pic = "Base/PFPZ/WPnone.jpg"
    PFP = Image.open(user_pic)
    PFP = PFP.resize((320,320))
    i1.paste(PFP, (355,255))
    
    square = Image.open("downloads/stk.jpg")
    i1.paste(square, (-20,210), mask=square)
    draw = ImageDraw.Draw(i1)
    draw.text((20, 20), f"[{message.from_user.id}] | @AnimeChatCommunity\n{message.date}", fill="black", stroke_width=10, stroke_fill="white")
    i1.save(f"downloads/pic1.jpg")
