from src.misc import app
from pyrogram import filters
from loguru import logger

"""

Добавляет голсовое сообщение

+гс <название гс> + <reply_message>

"""

@app.on_message(filters.command('гс',prefixes='+') & filters.me)
async def audio_add(client,message):
    try:
        text = message.text.split('+гс ')[1]
        await app.download_media(message.reply_to_message.voice.file_id,file_name=f'gs/{text}.ogg')
        logger.opt(colors=True).info(
            f"<green>Сохранено голосовое сообщение в чате: {message.chat.id} с названием '{text}'</green>"
        )
        await message.edit(f'✅Голосовое сообщение с именем "{text}"\nуспешно сохранено.')
    except:
        logger.opt(colors=True).error(
            f"<red>Ошибка при использовании '+гс' в чате: {message.chat.id}</red>"
        )
        await message.edit(f'⚠️Произошла неизвестная ошибка.')