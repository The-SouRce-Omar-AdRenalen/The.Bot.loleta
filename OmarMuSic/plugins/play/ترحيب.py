#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅    

import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from OmarMuSic import app
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatPermissions
from OmarMuSic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters


@app.on_message(filters.new_chat_members)
async def wel__come(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"- نورت ياا فرتكهه😘🤝️ {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",chat_id=chatid)
	
@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"- مشيت ليه يوحش يلا بسلامات🥲👋\n│ \n└ʙʏ  {message.from_user.mention} ",chat_id=chatid)
	

#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅    
