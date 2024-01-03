from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    html_content = """
    <h3 id="𝗚𝗥𝗢𝗨𝗣-𝗥𝗨𝗟𝗘𝗦-&amp;amp;-𝗣𝗨𝗡𝗜𝗦𝗛𝗠𝗘𝗡𝗧𝗦"><strong>𝗚𝗥𝗢𝗨𝗣 𝗥𝗨𝗟𝗘𝗦 &amp; 𝗣𝗨𝗡𝗜𝗦𝗛𝗠𝗘𝗡𝗧𝗦</strong></h3><figure><img src="/file/2fec9c65e4cf5dd58b370.mp4"/><figcaption>ABOUT~</figcaption></figure><p><strong>𝘼𝙣 𝙞𝙣𝙙𝙚𝙥𝙚𝙣𝙙𝙚𝙣𝙩 𝙘𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙗𝙖𝙨𝙚𝙙 𝙜𝙧𝙤𝙪𝙥 𝙢𝙖𝙙𝙚 𝙛𝙤𝙧 𝙩𝙝𝙚 𝙪𝙨𝙚𝙧𝙨 𝙩𝙤 𝙨𝙤𝙘𝙞𝙖𝙡𝙞𝙯𝙚, 𝙝𝙖𝙫𝙚 𝙤𝙥𝙚𝙣 𝙙𝙞𝙨𝙘𝙪𝙨𝙨𝙞𝙤𝙣 𝙖𝙣𝙙 𝙨𝙝𝙖𝙧𝙚 𝙩𝙝𝙚𝙞𝙧 𝙚𝙭𝙥𝙚𝙧𝙞𝙚𝙣𝙘𝙚𝙨;</strong>\n𝙈𝙤𝙨𝙩𝙡𝙮 𝙖𝙗𝙤𝙪𝙩<strong> Anime, Manga, Games, Musics, Memes, Arts and Otaku Culture.</strong></p><p><strong>ʀᴇᴍᴇᴍʙᴇʀ:</strong></p><blockquote><strong>» ᴛʜɪꜱ ɪꜱ ᴀ ᴄᴏᴍᴍᴜɴɪᴛʏ ɴᴏᴛ ᴀɴ ᴏʀɢᴀɴɪꜱᴀᴛɪᴏɴ, ɢᴀɴɢ, ᴄʟᴜʙ, ꜰᴇᴅᴇʀᴀᴛɪᴏɴ ᴏʀ ᴄᴏᴜɴᴄɪʟ, ɴᴏʀ ɪᴛ&#x27;ꜱ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴀɴʏ!</strong></blockquote><blockquote><strong>» ᴀʟʟ ᴛʜᴇ ʀᴜʟᴇꜱ ᴀʀᴇ ᴇɴꜰᴏʀᴄᴇᴅ ꜰᴏʀ ᴘʀᴏᴘᴇʀ ꜰᴜɴᴄᴛɪᴏɴɪɴɢ ᴏꜰ ɢʀᴏᴜᴘ ᴀɴᴅ ᴡᴇʟꜰᴀʀᴇ ᴏꜰ ᴍᴇᴍʙᴇʀꜱ.</strong></blockquote><blockquote><strong>» ᴀᴅᴍɪɴꜱ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴄʟᴇᴀʀ ᴠᴇʀʙᴀʟ ᴡᴀʀɴɪɴɢ ʙᴇꜰᴏʀᴇ ᴀᴘᴘʟʏɪɴɢ ᴀɴʏ ᴘᴜɴɪꜱʜᴍᴇɴᴛꜱ.</strong></blockquote><p></p><figure><img src="/file/761e5ba7845455cf623d9.jpg"/><figcaption>RULES</figcaption></figure><h3 id="𝟭❯-𝗨𝘀𝗲-𝗘𝗡𝗚𝗟𝗜𝗦𝗛-𝗢𝗡𝗟𝗬-&amp;#33;">𝟭❯<strong> 𝗨𝘀𝗲 𝗘𝗡𝗚𝗟𝗜𝗦𝗛 𝗢𝗡𝗟𝗬 !</strong></h3><p><strong>This is an international group </strong><em><strong>(people are here from around the world)</strong></em><strong> you cannot mix languages.</strong>\n<strong>You must always use english here, No matter how broken it is, </strong>or USE GOOGLE TRANSLATOR.</p><ul><li><strong>No restriction on media &amp; voice chat.</strong></li><li><strong>Few words will be permitted, like greetings... (only occasionally)</strong></li><li><strong><strong>Using Another language under filter isn&#x27;t exception.</strong></strong></li></ul><blockquote>Punishment:\n<strong>Warn (1/4)</strong>\n<strong>Mute (2 hours)</strong></blockquote><hr/><h3 id="𝟮❯-𝗕𝗲-𝗖𝗜𝗩𝗜𝗟-𝗼𝗿-𝗕𝗲-𝗕𝗔𝗡𝗡𝗘𝗗-&amp;#33;"><strong>𝟮❯ 𝗕𝗲 𝗖𝗜𝗩𝗜𝗟 𝗼𝗿 𝗕𝗲 𝗕𝗔𝗡𝗡𝗘𝗗 !</strong></h3><p><strong>We cannot restrict you from having arguments but we want to keep our community peaceful as much as possible therefore:</strong></p><ul><li><strong>Don&#x27;t post controversial stuff for unnecessary debate.</strong></li><li><strong>No hate speach towards races / religions etc. or any kind of discrimination / criticism</strong>.</li><li><strong>Don&#x27;t be rude/sarcastic to the members who may not be chill with you.</strong></li><li><strong>No Bullying, Constantly trolling or Hate comments to anyone.</strong></li></ul><blockquote>Punishment:\n<strong>Warn (1/4) for new ones.</strong>\n<strong>Mute (upto few weeks) if trouble causing. </strong>\n<strong>Ban (Permanent) for toxic mfs.</strong></blockquote><hr/><h3 id="𝟯❯-𝗡𝗼-(𝗔𝗱𝘃𝗲𝗿𝘁𝗶𝘀𝗲𝗺𝗲𝗻𝘁,-𝗦𝗽𝗮𝗺,-𝗦𝗰𝗮𝗺)">𝟯❯ <strong>𝗡𝗼 (𝗔𝗱𝘃𝗲𝗿𝘁𝗶𝘀𝗲𝗺𝗲𝗻𝘁, 𝗦𝗽𝗮𝗺, 𝗦𝗰𝗮𝗺</strong>)</h3><ul><li><strong>We do not allow any kinds of promotion activity or advertisement material of other groups and channels in chat, refrain from doing that.</strong></li><li><strong>Also,</strong> <strong>Asking people to join or follow your stuff in group or messaging members privately for that can lead to permanent ban.</strong></li><li><strong>Be aware that</strong> <strong>Selling Netflix or Crunchyroll accounts ,</strong><strong> </strong><strong><strong>job opportunities</strong></strong><strong> , </strong><strong>airdrops / giveaways</strong><strong> </strong>, <strong>crypto </strong><strong>is considered to be SCAM and leads to permanent mute.</strong></li></ul><blockquote>Punishment:\n<strong>Mute (48 hours)</strong>\n<strong>Ban (permanent)</strong></blockquote><hr/><h3 id="𝟰❯-𝗠𝗲𝗱𝗶𝗮-𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀">𝟰❯ <strong>𝗠𝗲𝗱𝗶𝗮 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀</strong></h3><p>It&#x27;s strictly forbidden to send messages or to have profile with media containing:</p><p>× Generic NSFW 🔞\n× Porn material 🔞\n× Child pornography ⚠️\n× Any Sensitive or gore material 🩸\n× Violence or Criticism ☣️\n× Yaoi or LGBTQ 🏳️\u200d🌈\n× Epileptic contents 🧠</p><blockquote>Punishment:\n<strong>Ban (permanent)</strong></blockquote><hr/><h3 id="𝟱❯-𝗡𝗼-(𝗙𝗹𝗼𝗼𝗱𝗶𝗻𝗴,-𝗕𝗼𝗼𝘀𝘁-𝗮𝗰𝘁𝗶𝗼𝗻𝘀,-𝗨𝘀𝗲𝗿𝗯𝗼𝘁𝘀)">𝟱❯<strong> 𝗡𝗼 (𝗙𝗹𝗼𝗼𝗱𝗶𝗻𝗴, 𝗕𝗼𝗼𝘀𝘁 𝗮𝗰𝘁𝗶𝗼𝗻𝘀</strong>, 𝗨𝘀𝗲𝗿𝗯𝗼𝘁𝘀)</h3><p>E<strong>xtensive spam of media or Flooding</strong>, 𝗿𝗮𝗶𝗱𝘀, 𝗯𝗼𝗼𝘀𝘁 𝗮𝗰𝘁𝗶𝗼𝗻𝘀<strong>,</strong> <strong>are</strong> 𝘀𝘁𝗿𝗶𝗰𝘁𝗹𝘆 𝗽𝗿𝗼𝗵𝗶𝗯𝗶𝘁𝗲𝗱.</p><ul><li>Sending multiple messages in short interval of time is considered spam.</li><li><strong>Don&#x27;t spam bot command use them responsibly.</strong></li><li><strong>Don&#x27;t post any external links or forward message from channels.</strong></li><li><strong>For involvement in raids, mass add and boost Actions such as inviting teams for arguments, all the suspected accounts will be banned</strong></li><li><strong>It&#x27;s strictly forbidden the use of userbots, user-optimized accounts with public commands, messaging through channel account or any other kind of actions that could tarnish recent actions.</strong></li></ul><blockquote>Punishment:\n<strong>Warn (1/4)</strong>\n<strong>Mute (48 hours)</strong>\n<strong>Ban (permanent, applicable for last 2 points only)</strong></blockquote><hr/><h3 id="𝟲❯-𝗥𝗲𝘀𝗽𝗲𝗰𝘁𝗳𝘂𝗹-𝗖𝗼𝗺𝗺𝘂𝗻𝗶𝗰𝗮𝘁𝗶𝗼𝗻">𝟲❯ 𝗥𝗲𝘀𝗽𝗲𝗰𝘁𝗳𝘂𝗹 𝗖𝗼𝗺𝗺𝘂𝗻𝗶𝗰𝗮𝘁𝗶𝗼𝗻</h3><ul><li>Public<strong> criticism or mockery of members under any circumstances will not be tolerated!</strong> <em>everyone has his/her own ideas and thoughts, must be respected for them</em>.</li><li><strong>Any kind of profanity or talking dirty with girls, or insults and abuse to members</strong><strong> is strictly prohibited</strong>!</li><li>This is not a dating site to find your life partner here. Avoid sending cringe message and media, or messeging someone personally and annoying them.</li></ul><blockquote>Punishment:\n<strong>Warn (1/4)</strong>\n<strong>Mute (upto few months)</strong></blockquote><hr/><h3 id="𝟳❯-𝗩𝗼𝗶𝗰𝗲-𝗖𝗵𝗮𝘁-𝗥𝘂𝗹𝗲𝘀">𝟳❯ <strong>𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁 𝗥𝘂𝗹𝗲𝘀 </strong></h3><ol><li>There is no language restriction in VC (as for now) you can talk in your desired languages, Still its adviced to use English so everyone can engage.</li><li>Violation of RULE-2 (i.e. abusive behaviour) will not be tolerated, you&#x27;ll be muted permanently in vc.</li><li>Inviting members to other groups through vc will result in permanent ban.</li><li>Streaming Any Content That Violates RULE-4 (any nsfw media or improper content) will result in permanent BAN.</li><li>Joining as channel is not allowed, your channel will be banned instantly. (only channel will be removed not your account)</li><li>Playing music is not allowed while people are talking. You can play songs rest of the time.</li><li>Music bot (skip, pause, etc) permissions are allowed for everyone but you need to ask admin to authorise you, but if you&#x27;re reported for misusing these rights you&#x27;ll be immediately unauthorised permanently.</li></ol><blockquote>Punishment:\n<strong>Warn (1/4)</strong>\n<strong>Mute (48 hours in vc)</strong></blockquote><hr/><h3 id="𝗥𝘂𝗹𝗲-𝗭𝗲𝗿𝗼"><strong>𝗥𝘂𝗹𝗲 𝗭𝗲𝗿𝗼</strong></h3><h4 id="The-admins-assume-the-right-to-be-able-to-apply-a-restriction-to-users-who-carry-out-any-type-of-behavior-not-appropriate-to-the-civil-quiet-in-the-group-and-not-described-in-the-regulation.">The admins assume the right to be able to apply a restriction to users who carry out any type of behavior not appropriate to the civil quiet in the group and not described in the regulation.</h4><hr/><p>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ</p><figure><img src="/file/98ce9230b450439bebd24.jpg"/><figcaption></figcaption></figure><h4 id="𐂡-𝙏𝙝𝙚-𝙘𝙝𝙤𝙞𝙘𝙚-𝙤𝙛-𝙥𝙪𝙣𝙞𝙨𝙝𝙢𝙚𝙣𝙩𝙨-𝙛𝙤𝙧-𝙩𝙝𝙤𝙨𝙚-𝙬𝙝𝙤-𝙫𝙞𝙤𝙡𝙖𝙩𝙚-𝙩𝙝𝙚-𝙧𝙚𝙜𝙪𝙡𝙖𝙩𝙞𝙤𝙣-𝙖𝙣𝙙-𝙩𝙝𝙚-𝙙𝙪𝙧𝙖𝙩𝙞𝙤𝙣-𝙤𝙛-𝙩𝙝𝙚𝙢-𝙞𝙨-𝙖𝙩-𝙩𝙝𝙚-𝙩𝙤𝙩𝙖𝙡-𝙙𝙞𝙨𝙘𝙧𝙚𝙩𝙞𝙤𝙣-𝙤𝙛-𝙩𝙝𝙤𝙨𝙚-𝙬𝙝𝙤-𝙖𝙥𝙥𝙡𝙮-𝙩𝙝𝙚𝙢&amp;#33;-ᴅᴇᴘᴇɴᴅɪɴɢ-ᴏɴ-ꜱɪᴛᴜᴀᴛɪᴏɴ."><strong>𐂡 𝙏𝙝𝙚 𝙘𝙝𝙤𝙞𝙘𝙚 𝙤𝙛 𝙥𝙪𝙣𝙞𝙨𝙝𝙢𝙚𝙣𝙩𝙨 𝙛𝙤𝙧 𝙩𝙝𝙤𝙨𝙚 𝙬𝙝𝙤 𝙫𝙞𝙤𝙡𝙖𝙩𝙚 𝙩𝙝𝙚 𝙧𝙚𝙜𝙪𝙡𝙖𝙩𝙞𝙤𝙣 𝙖𝙣𝙙 𝙩𝙝𝙚 𝙙𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙤𝙛 𝙩𝙝𝙚𝙢 𝙞𝙨 𝙖𝙩 𝙩𝙝𝙚 𝙩𝙤𝙩𝙖𝙡 𝙙𝙞𝙨𝙘𝙧𝙚𝙩𝙞𝙤𝙣 𝙤𝙛 𝙩𝙝𝙤𝙨𝙚 𝙬𝙝𝙤 𝙖𝙥𝙥𝙡𝙮 𝙩𝙝𝙚𝙢! </strong>ᴅᴇᴘᴇɴᴅɪɴɢ ᴏɴ ꜱɪᴛᴜᴀᴛɪᴏɴ.</h4><h4 id="𐂡-𝙒𝙖𝙧𝙣𝙨-𝙖𝙧𝙚-𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩,-𝙞𝙩-𝙬𝙞𝙡𝙡-𝙤𝙣𝙡𝙮-𝙗𝙚-𝙧𝙚𝙢𝙤𝙫𝙚𝙙-𝙖𝙛𝙩𝙚𝙧-𝙧𝙚𝙖𝙘𝙝𝙞𝙣𝙜-(𝟒/𝟒)-𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙙-𝙗𝙮-𝟐-𝙙𝙖𝙮𝙨-𝙤𝙛-𝙙𝙚𝙩𝙚𝙣𝙩𝙞𝙤𝙣."><strong>𐂡 𝙒𝙖𝙧𝙣𝙨 𝙖𝙧𝙚 𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩, 𝙞𝙩 𝙬𝙞𝙡𝙡 𝙤𝙣𝙡𝙮 𝙗𝙚 𝙧𝙚𝙢𝙤𝙫𝙚𝙙 𝙖𝙛𝙩𝙚𝙧 𝙧𝙚𝙖𝙘𝙝𝙞𝙣𝙜 (𝟒/𝟒) 𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙙 𝙗𝙮 𝟐 𝙙𝙖𝙮𝙨 𝙤𝙛 𝙙𝙚𝙩𝙚𝙣𝙩𝙞𝙤𝙣.</strong></h4><h4 id="𐂡-𝘿𝙚𝙛𝙖𝙪𝙡𝙩-𝙢𝙪𝙩𝙚-𝙗𝙮-𝘽𝙤𝙩-(𝟒-𝙬𝙖𝙧𝙣𝙨)-𝙞𝙨-𝙛𝙤𝙧-𝟒𝟖-𝙝𝙤𝙪𝙧𝙨.-(ᴍɪɴɪᴍᴜᴍ)"><strong>𐂡 𝘿𝙚𝙛𝙖𝙪𝙡𝙩 𝙢𝙪𝙩𝙚 𝙗𝙮 𝘽𝙤𝙩 (𝟒 𝙬𝙖𝙧𝙣𝙨) 𝙞𝙨 𝙛𝙤𝙧 𝟒𝟖 𝙝𝙤𝙪𝙧𝙨. </strong>(ᴍɪɴɪᴍᴜᴍ)</h4><h4 id="𐂡-𝘿𝙚𝙛𝙖𝙪𝙡𝙩-𝙢𝙪𝙩𝙚-𝙗𝙮-𝙖𝙙𝙢𝙞𝙣𝙨-𝙞𝙨-𝙛𝙤𝙧-𝟗𝟔-𝙝𝙤𝙪𝙧𝙨.-(ᴍɪɴɪᴍᴜᴍ)"><strong>𐂡 𝘿𝙚𝙛𝙖𝙪𝙡𝙩 𝙢𝙪𝙩𝙚 𝙗𝙮 𝙖𝙙𝙢𝙞𝙣𝙨 𝙞𝙨 𝙛𝙤𝙧 𝟗𝟔 𝙝𝙤𝙪𝙧𝙨. </strong>(ᴍɪɴɪᴍᴜᴍ)</h4><h4 id="𐂡-𝙈𝙪𝙡𝙩𝙞𝙥𝙡𝙚-𝙢𝙪𝙩𝙚𝙨-𝙬𝙞𝙡𝙡-𝙧𝙚𝙨𝙪𝙡𝙩-𝙞𝙣-𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩-𝘽𝘼𝙉."><strong>𐂡 𝙈𝙪𝙡𝙩𝙞𝙥𝙡𝙚 𝙢𝙪𝙩𝙚𝙨 𝙬𝙞𝙡𝙡 𝙧𝙚𝙨𝙪𝙡𝙩 𝙞𝙣 𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩 𝘽𝘼𝙉.</strong></h4><h4 id="𐂡-𝘽𝙖𝙣𝙨-𝙖𝙧𝙚-𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩-𝙬𝙚-𝙙𝙤𝙣&amp;#39;𝙩-𝙪𝙣𝙗𝙖𝙣-𝙖𝙣𝙮𝙤𝙣𝙚."><strong>𐂡 𝘽𝙖𝙣𝙨 𝙖𝙧𝙚 𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩 𝙬𝙚 𝙙𝙤𝙣&#x27;𝙩 𝙪𝙣𝙗𝙖𝙣 𝙖𝙣𝙮𝙤𝙣𝙚.</strong></h4><h4 id="𐂡-𝘼𝙡𝙡-𝙖𝙙𝙢𝙞𝙣𝙨-𝙩𝙖𝙠𝙚-𝙩𝙝𝙚𝙞𝙧-𝙖𝙘𝙩𝙞𝙤𝙣𝙨-𝙫𝙚𝙧𝙮-𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙫𝙚𝙡𝙮.-ᴅᴏɴ&amp;#39;ᴛ-ᴀʀɢᴜᴇ-ᴏʀ-ᴍᴇꜱꜱᴀɢᴇ-ᴛʜᴇᴍ-ᴘʀɪᴠᴀᴛᴇʟʏ-ᴛᴏ-ʀᴇᴍᴏᴠᴇ-ʀᴇꜱᴛʀɪᴄᴛɪᴏɴꜱ,-ᴡᴀɪᴛ-ᴘᴀᴛɪᴇɴᴛʟʏ-ꜰᴏʀ-PUNISHMENT-ᴘᴇʀɪᴏᴅ-ᴛᴏ-ᴏᴠᴇʀ."><strong>𐂡 𝘼𝙡𝙡 𝙖𝙙𝙢𝙞𝙣𝙨 𝙩𝙖𝙠𝙚 𝙩𝙝𝙚𝙞𝙧 𝙖𝙘𝙩𝙞𝙤𝙣𝙨 𝙫𝙚𝙧𝙮 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙫𝙚𝙡𝙮. ᴅᴏɴ&#x27;ᴛ ᴀʀɢᴜᴇ ᴏʀ ᴍᴇꜱꜱᴀɢᴇ ᴛʜᴇᴍ ᴘʀɪᴠᴀᴛᴇʟʏ ᴛᴏ ʀᴇᴍᴏᴠᴇ ʀᴇꜱᴛʀɪᴄᴛɪᴏɴꜱ, ᴡᴀɪᴛ ᴘᴀᴛɪᴇɴᴛʟʏ ꜰᴏʀ PUNISHMENT</strong> ᴘᴇʀɪᴏᴅ ᴛᴏ ᴏᴠᴇʀ.</h4><h4 id="𐂡-𝙒𝙚-𝙠𝙚𝙚𝙥-𝙩𝙧𝙖𝙘𝙠-𝙤𝙛-𝙚𝙫𝙚𝙧𝙮-𝙖𝙙𝙢𝙞𝙣-𝙖𝙘𝙩𝙞𝙤𝙣-𝙖𝙣𝙙-𝙢𝙚𝙢𝙗𝙚𝙧𝙨-𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮,-𝙖𝙡𝙤𝙣𝙜-𝙬𝙞𝙩𝙝-𝙮𝙤𝙪𝙧-𝙐𝙄𝘿-𝙖𝙨-𝙜𝙧𝙤𝙪𝙥-𝙡𝙤𝙜𝙨."><strong>𐂡 𝙒𝙚 𝙠𝙚𝙚𝙥 𝙩𝙧𝙖𝙘𝙠 𝙤𝙛 𝙚𝙫𝙚𝙧𝙮 𝙖𝙙𝙢𝙞𝙣 𝙖𝙘𝙩𝙞𝙤𝙣 𝙖𝙣𝙙 𝙢𝙚𝙢𝙗𝙚𝙧𝙨 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮, 𝙖𝙡𝙤𝙣𝙜 𝙬𝙞𝙩𝙝 𝙮𝙤𝙪𝙧 𝙐𝙄𝘿 𝙖𝙨 𝙜𝙧𝙤𝙪𝙥 𝙡𝙤𝙜𝙨.</strong></h4><h4 id="𐂡-𝙉𝙤𝙣𝙚-𝙤𝙛-𝙩𝙝𝙚-𝘼𝙙𝙢𝙞𝙣𝙨-𝙖𝙧𝙚-𝙨𝙪𝙥𝙚𝙧𝙞𝙤𝙧-𝙩𝙤-𝙮𝙤𝙪.-𝘼𝙙𝙢𝙞𝙣𝙨-𝙖𝙧𝙚-𝙢𝙖𝙙𝙚-𝙟𝙪𝙨𝙩-𝙩𝙤-𝙢𝙤𝙙𝙚𝙧𝙖𝙩𝙚-𝙩𝙝𝙚-𝙘𝙝𝙖𝙩-𝙖𝙣𝙙-𝙥𝙧𝙚𝙫𝙚𝙣𝙩-𝙫𝙤𝙞𝙡𝙖𝙩𝙞𝙤𝙣-𝙤𝙛-𝙧𝙪𝙡𝙚𝙨."><strong>𐂡 𝙉𝙤𝙣𝙚 𝙤𝙛 𝙩𝙝𝙚 𝘼𝙙𝙢𝙞𝙣𝙨 𝙖𝙧𝙚 𝙨𝙪𝙥𝙚𝙧𝙞𝙤𝙧 𝙩𝙤 𝙮𝙤𝙪. 𝘼𝙙𝙢𝙞𝙣𝙨 𝙖𝙧𝙚 𝙢𝙖𝙙𝙚 𝙟𝙪𝙨𝙩 𝙩𝙤 𝙢𝙤𝙙𝙚𝙧𝙖𝙩𝙚 𝙩𝙝𝙚 𝙘𝙝𝙖𝙩 𝙖𝙣𝙙 𝙥𝙧𝙚𝙫𝙚𝙣𝙩 𝙫𝙤𝙞𝙡𝙖𝙩𝙞𝙤𝙣 𝙤𝙛 𝙧𝙪𝙡𝙚𝙨.</strong></h4><h4 id="𐂡-𝙉𝙤𝙣𝙚-𝙤𝙛-𝙖𝙙𝙢𝙞𝙣𝙨-𝙝𝙖𝙫𝙚-𝙩𝙞𝙢𝙚-𝙩𝙤-𝙡𝙤𝙤𝙠-𝙩𝙝𝙧𝙤𝙪𝙜𝙝-𝙮𝙤𝙪𝙧-𝙖𝙛𝙛𝙖𝙞𝙧𝙨,-(𝙬𝙝𝙤-𝙨𝙩𝙖𝙧𝙩𝙚𝙙-𝙛𝙤𝙧-𝙬𝙝𝙖𝙩-𝙘𝙖𝙪𝙨𝙚)-𝙔𝙤𝙪-𝙢𝙪𝙨𝙩-𝙧𝙚𝙥𝙤𝙧𝙩-𝙞𝙣𝙨𝙩𝙚𝙖𝙙-𝙤𝙛-𝙛𝙞𝙜𝙝𝙩𝙞𝙣𝙜-𝙮𝙤𝙪𝙧𝙨𝙚𝙡𝙛.-𝙞𝙛-𝙮𝙤𝙪-𝙜𝙤𝙩-𝙘𝙖𝙪𝙜𝙝𝙩-𝙬𝙝𝙞𝙡𝙚-𝙖𝙗𝙪𝙨𝙞𝙣𝙜-𝙩𝙝𝙖𝙩&amp;#39;𝙨-𝙮𝙤𝙪𝙧-𝙤𝙬𝙣-𝙜𝙤𝙙-𝙙𝙖𝙢𝙣-𝙥𝙧𝙤𝙗𝙡𝙚𝙢.">𐂡 𝙉𝙤𝙣𝙚 𝙤𝙛 𝙖𝙙𝙢𝙞𝙣𝙨 𝙝𝙖𝙫𝙚 𝙩𝙞𝙢𝙚 𝙩𝙤 𝙡𝙤𝙤𝙠 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙮𝙤𝙪𝙧 𝙖𝙛𝙛𝙖𝙞𝙧𝙨, (𝙬𝙝𝙤 𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙛𝙤𝙧 𝙬𝙝𝙖𝙩 𝙘𝙖𝙪𝙨𝙚) 𝙔𝙤𝙪 𝙢𝙪𝙨𝙩 𝙧𝙚𝙥𝙤𝙧𝙩 𝙞𝙣𝙨𝙩𝙚𝙖𝙙 𝙤𝙛 𝙛𝙞𝙜𝙝𝙩𝙞𝙣𝙜 𝙮𝙤𝙪𝙧𝙨𝙚𝙡𝙛. 𝙞𝙛 𝙮𝙤𝙪 𝙜𝙤𝙩 𝙘𝙖𝙪𝙜𝙝𝙩 𝙬𝙝𝙞𝙡𝙚 𝙖𝙗𝙪𝙨𝙞𝙣𝙜 𝙩𝙝𝙖𝙩&#x27;𝙨 𝙮𝙤𝙪𝙧 𝙤𝙬𝙣 𝙜𝙤𝙙 𝙙𝙖𝙢𝙣 𝙥𝙧𝙤𝙗𝙡𝙚𝙢.</h4><h4 id="𐂡-𝙎𝙚𝙣𝙙𝙞𝙣𝙜-𝙡𝙞𝙣𝙠𝙨-𝙤𝙧-𝙛𝙤𝙧𝙬𝙖𝙧𝙙𝙞𝙣𝙜-𝙢𝙚𝙨𝙨𝙖𝙜𝙚-𝙧𝙚𝙡𝙖𝙩𝙚𝙙-𝙩𝙤-𝙖𝙣𝙞𝙢𝙚,-𝙞𝙨-𝙖𝙡𝙡𝙤𝙬𝙚𝙙-𝙗𝙪𝙩-𝙮𝙤𝙪-𝙣𝙚𝙚𝙙-𝙩𝙤-𝙗𝙚-𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙨𝙚𝙙-𝙗𝙮-𝙖𝙙𝙢𝙞𝙣𝙨."><strong>𐂡 𝙎𝙚𝙣𝙙𝙞𝙣𝙜 𝙡𝙞𝙣𝙠𝙨 𝙤𝙧 𝙛𝙤𝙧𝙬𝙖𝙧𝙙𝙞𝙣𝙜 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙧𝙚𝙡𝙖𝙩𝙚𝙙 𝙩𝙤 𝙖𝙣𝙞𝙢𝙚, 𝙞𝙨 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙗𝙪𝙩 𝙮𝙤𝙪 𝙣𝙚𝙚𝙙 𝙩𝙤 𝙗𝙚 𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙨𝙚𝙙 𝙗𝙮 𝙖𝙙𝙢𝙞𝙣𝙨.</strong></h4><h4 id="𐂡-𝙏𝙮𝙥𝙚-/links-𝙩𝙤-𝙖𝙘𝙘𝙚𝙨𝙨-𝙘𝙝𝙖𝙣𝙣𝙚𝙡𝙨-𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙚𝙙-𝙩𝙤-𝙪𝙨."><strong>𐂡 𝙏𝙮𝙥𝙚</strong> /links <strong>𝙩𝙤 𝙖𝙘𝙘𝙚𝙨𝙨 𝙘𝙝𝙖𝙣𝙣𝙚𝙡𝙨 𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙚𝙙 𝙩𝙤 𝙪𝙨.</strong></h4><p>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ</p><figure><img src="/file/784630817c415cc86a2da.jpg"/><figcaption></figcaption></figure><p>All rules can be accessed in chat by command: /r followed by number of rule (<em>to inform new members when necessary or before report</em>)</p><blockquote>type:  /listrules for more info</blockquote><p><em>SOME EXTRA COMMANDS~~~</em></p><ul><li><strong>/english</strong> - <em>bish english plz</em></li><li><strong>/listrules</strong> - <em>list all commands</em></li><li><strong>/nsfwpfp</strong> - <em>hide nsfw pfp from group</em></li><li><strong>/punishment</strong> or <strong>!precept</strong> - <em>Things you should know.</em></li><li><strong>/blocklist</strong> - <em>what&#x27;s blacklisted user</em></li><li>/links - links of other channels &amp; groups </li><li>/spam - spam group link</li><li>/agc - admins group link</li><li>/ty - thanks</li></ul><p>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ</p><hr/><h3 id="𝐍𝐄𝐗𝐓-⎘-[-𝙿𝙰𝙶𝙴-2-]-#-Reports-and-Assistance"><strong><strong><a href="/AnimeCommunityChat-Reports--Assistance-10-05">𝐍𝐄𝐗𝐓 ⎘ [ 𝙿𝙰𝙶𝙴 2 ] # Reports and Assistance</a></strong></strong></h3><hr/><h3 id="𝐍𝐄𝐗𝐓-⎘-[-𝙿𝙰𝙶𝙴-3-]-#-Few-Extra-Guidelines"><a href="/Anime-Chat-Community-English-12-27"><strong>𝐍𝐄𝐗𝐓 ⎘ [ 𝙿𝙰𝙶𝙴 3 ] # Few Extra Guidelines </strong></a></h3><hr/><p>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ</p><p><em>Update V3:</em> <strong>October 5, 2023 (by emi)</strong>\n<em>Update V2:</em> <strong>January 1, 2023 (by emi)</strong>\n<em>Update V1:</em> <strong>August 30, 2022 (by dsp)</strong>\n<em>First Published:</em> <strong>June 17, 2022 (by emi)</strong></p><p><a href="https://t.me/+gvV1K5MzVqExMjVl" target="_blank">Anime Chat Community [English]</a> © since 2020</p><p>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ</p><p><br/></p>
    """
    return web.Response(text=html_content, content_type="text/html")
    #return web.json_response("Animerobots")
