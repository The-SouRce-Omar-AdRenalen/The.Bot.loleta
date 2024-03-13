from pyrogram import filters
from pyrogram.types import Message

from OmarMuSic import app
from OmarMuSic.core.call import Mody
from OmarMuSic.utils.database import is_music_playing, music_off
from OmarMuSic.utils.decorators import AdminRightsCheck
from OmarMuSic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Mody.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )