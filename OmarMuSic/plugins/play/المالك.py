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
from OmarMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from OmarMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait








@app.on_message(filters.command(["السورس ","سورس","مصنع"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09d9ee4d37a065e62396b.jpg",
        caption=f"""╭── • ⌯ [𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑](https://t.me/DEV_ADRENALEN) ⌯ • ──╮\n• ⌯ [𝐒𝐔𝐏𝐏𝐔𝐑𝐓.𝐒𝐎𝐔𝐑𝐂𝐄](https://t.me/BaR_AdRenalen) ⌯ •\n • ⌯ [𝐂𝐇𝐀𝐍𝐍𝐄𝐋.𝐒𝐎𝐔𝐑𝐂𝐄](https://t.me/WA_AdRenalen) ⌯ •\n• ⌯ [𝐁𝐎𝐓.𝐄𝐋𝐒𝐎𝐔𝐑𝐂𝐄](https://t.me/Xx_MUOSIC_BOT)⌯ •\n╰── • ⌯ [𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑](https://t.me/DEV_ADRENALEN) ⌯ • ──╯""",
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
    


@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""), group=222)
async def ownner(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await app.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"**⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:`{message.from_user.id}`\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : `{message.chat.id}`**",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"**⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:`{message.from_user.id}`\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : `{message.chat.id}`**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("الاك محذوف يقلب")

iddof = []
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
    await message.reply_photo(photo,       caption=f"""**⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:`{message.from_user.id}`\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : `{message.chat.id}`**""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    



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
       


@app.on_message(filters.command(["اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""🥀❄️ اسمك »»  `{message.from_user.mention}`""") 
