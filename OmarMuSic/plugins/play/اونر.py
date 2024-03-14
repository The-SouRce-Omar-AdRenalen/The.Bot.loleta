#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅
import asyncio
import os
import time
import requests
from pyrogram import enums
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from OmarMuSic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from OmarMuSic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
##############################################################
##############################################################
##############################################################

@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك : {message.from_user.mention()} 🥹💘 ⋅""") 
##############################################################
##############################################################
##############################################################
@app.on_message(filters.command([" السورس ","سورس"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09d9ee4d37a065e62396b.jpg",
        caption=f"""• ⌯ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑 ⌯ •\n\n- 𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 𝐁𝐎𝐓 𝐎𝐍 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐒𝐔𝐏𝐄𝐑 𝐅𝐀𝐒𝐓 𝐀𝐍𝐃 𝐇𝐈𝐆𝐇 𝐀𝐂𝐂𝐔𝐑𝐀𝐂𝐘 ❤️🌿 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑 › ", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ›", url=f"https://t.me/WA_AdRenalen"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓 ›", url=f"https://t.me/BAR_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )
##############################################################
##############################################################
##############################################################

@app.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"], ""), group=2272)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("تم معطل من قبل🔒")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], ""), group=2292)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل ✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح الايدي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(filters.command(["ايدي","الايدي","ا"], ""), group=27722)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""🤡 ¦𝙽𝙰𝙼𝙴 :{message.from_user.mention}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{message.from_user.username}\n🎃 ¦𝙸𝙳 :{message.from_user.id}\n💌 ¦𝙱𝙸𝙾 :{usr.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :{message.chat.id}""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    
##############################################################
##############################################################
##############################################################

iddof = []
@app.on_message(filters.command(["قفل جمالي", "تعطيل جمالي"], ""), group=22332)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("جمالي معطل من قبل✅")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل جمالي بنجاح✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["قفل جمالي", "تعطيل جمالي"], ""), group=222009)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("جمالي مفعل من قبل✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح جمالي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(filters.command(["جمالي","جمالو","ج"], ""), group=22452)
async def iddyyyd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n│ \n└ʙʏ: {ik} %😂🥀❄️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
   
#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅    