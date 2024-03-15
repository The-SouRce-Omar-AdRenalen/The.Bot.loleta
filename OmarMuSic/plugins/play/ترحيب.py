import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from OmarMuSic import app
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatPermissions
from OmarMuSic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters

abd = types.InlineKeyboardMarkup()
abdd = types.InlineKeyboardButton(text = "$ch.",url="t.me/WA_ADRENALEN")
abd.add(abdd)
abod = telebot.TeleBot('5043466517:')
@abod.message_handler(content_types=['new_chat_members'])
def delete_join(message):
	j = message.chat.title
	f2 = message.from_user.first_name
	t2 = message.from_user.username
	id = message.from_user.id
	t = time.strftime("%Y/%m/%d")
	abod.reply_to(message,f"""*✵ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗠𝘆 𝗙𝗿𝗶𝗲𝗻𝗱 𝗶𝗻 {j}  🦋.
✵ 𝗬𝗼𝘂𝗿 𝗡𝗮𝗺𝗲 : {f2} 
✵ 𝗬𝗼𝘂𝗿 𝗨𝘀𝗲𝗿 : @{t2}
✵ 𝗝𝗼𝗶𝗻 𝗧𝗶𝗺𝗲 : {t}
*""",parse_mode="markdown",reply_markup=abd)
abod.polling()
