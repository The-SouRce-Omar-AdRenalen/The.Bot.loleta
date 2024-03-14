#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅


import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from OmarMuSic import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus


@app.on_message(command(['نداء','ن']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
         return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"ووين ككارس لنا واجد نرجو فيك 😾 {random_member_mention}",
        f"• يا قمري ❤️‍🔥 {random_member_mention}",
        f"حبي فوتك من الخاص وتعال 🤔 {random_member_mention}",
        f"• يا راس السطل تعال {random_member_mention}",
        f"• انت ليش قمر هكي 🌚♥ {random_member_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)


#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅