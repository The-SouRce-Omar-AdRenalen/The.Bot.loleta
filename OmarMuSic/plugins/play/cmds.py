#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅

import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from OmarMuSic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4a1e93b4660b7de2130c5.jpg",
        caption=f"""<b>» مرحباً بك عزيزي </b> {message.from_user.mention} .\n\n<b>» استخدم الازرار بالاسفل 𝄞\n» ل تصفح اوامر الميوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامر التشغيل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامر القناة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامر الادمن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامر المطور •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴.𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽", url="https://t.me/WA_ADRENALEN"),
                ],
            ]
        ),
    )


@app.on_message(command(["مطور", "المطور"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    async for photo in client.iter_profile_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ٴ<b>•────‌‌‏✯ ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
                    
- 𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :`{usr.id}`
 
ٴ<b>•────‌‌‏✯ _ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton("𝙳𝙴𝚅.𝚂𝙾𝚄𝚁𝙲𝙴.𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽", url="https://t.me/DEV_ADRENALEN"),
            ],
          ]
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    senderuser = message.from_user.username
                    sender_user = "@{senderuser}" if senderuser else "لا يوجد"
                    await app.send_message(OWNER_ID, f"- المستخدم {message.from_user.mention} يناديك \n\n- الاسم : {sender_name} \n- الايدي : {sender_id}\n- اليوزر : {sender_user}")
                    return await app.send_message(LOGGER_ID, f"- المستخدم {message.from_user.mention} يناديك \n\n- الاسم : {sender_name} \n- الايدي : {sender_id}\n- اليوزر : {sender_user}")
      
#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅