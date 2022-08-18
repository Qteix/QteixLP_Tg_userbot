from src.misc import app
from pyrogram import filters
from loguru import logger
from simpledemotivators import Demotivator
import os

"""
Делает демотиватор

.дем <reply_message_picture>

"""

@app.on_message(filters.command('дем',prefixes='.') & filters.me)
async def demotivator(client,message):
    logger.opt(colors=True).info(
            f"Использована комманда 'дем' в чате: {message.chat.id}"
        )
    await app.delete_messages(chat_id=message.chat.id,message_ids=message.id)
    await app.download_media(message.reply_to_message.photo.file_id,file_name='dem.png')
    text = message.text.split('.дем')[1]
    dem = Demotivator(f'{text}', '')
    dem.create('downloads/dem.png',font_name='arial.ttf')
    filename = "demresult.jpg"
    await app.send_photo(chat_id=message.chat.id,photo=filename,reply_to_message_id=message.reply_to_message_id)
    os.remove(filename)
