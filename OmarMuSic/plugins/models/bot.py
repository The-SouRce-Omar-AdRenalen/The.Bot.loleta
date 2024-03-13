#✘ ITALY MUSIC @I6ALY ✘
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
    button = InlineKeyboardButton("اضف البوت ال مجموعتك 🎸 ⋅ ", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 1924832439:
             rank = "**اللعب صاحب السورس بنفسو ف البار 🎸 ⋅**"
        elif user_id == OWNER_ID:
             rank = "مالك البوت يزميلي 🎸 ⋅"
        elif member.status == 'creator':
             rank = "**صاحب البار يزميلي 🎸 ⋅**"
        elif member.status == 'administrator':
             rank = "**مشرف كحيان 🎸 ⋅**"
        else:
             rank = "**عضو كحيان 🎸 ⋅**"
    except Exception as e:
        print(e)
        rank = "ملوش ملة لحد دلوقتي 🎸 ⋅"
    async for photo in client.iter_profile_photos("me", limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**نعم حبيبي :** {italy} 🥰❤\n**انا اسمي القميل :** {bot_name} 🥺🙈\n**رتبتك هي :** {rank}""", reply_markup=keyboard)

