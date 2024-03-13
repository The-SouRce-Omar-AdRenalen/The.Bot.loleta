#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅

import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from OmarMuSic import app
from config import OWNER_ID

@app.on_message(filters.command(['بوت'], prefixes=""))
async def OmarMuSic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك 🎸 ⋅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 1924832439:
             rank = "اللعب صاحب السورس بنفسو هنا 😂♥️ ،"
        elif user_id == OWNER_ID:
             rank = "مالك البوت يزميلي 🎸 ⋅"
        elif member.status == 'creator':
             rank = "صاحب البار يزمييلي 🎸 ⋅"
        elif member.status == 'administrator':
             rank = "مشرف البار يزميلي 🎸 ⋅"
        else:
             rank = "عضو كحيان 😂♥️ ،"
    except Exception as e:
        print(e)
        rank = "ملوش ملة دا 😂♥️ ،"
        await message.reply_text(
        text=f"""نعم حبيبي : {omar} 🥰❤️\n**انا اسمي القميل : {bot_name} 🥺🙈\n**رتبتك هي : {rank}""", reply_markup=keyboard)

#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅
