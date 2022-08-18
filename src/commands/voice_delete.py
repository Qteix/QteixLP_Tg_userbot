from src.misc import app
from pyrogram import filters
from loguru import logger
import os

"""

Удаляет голосовое сообщение

-гс <название гс>

"""

@app.on_message(filters.command('гс',prefixes='-') & filters.me)
async def gs_delete(client,message):
    try:
        text = message.text.split('-гс ')[1]
        os.remove(f'gs/{text}.ogg')

        logger.opt(colors=True).info(
            f"<green>Использована комманда '-гс' в чате : {message.chat.id}</green>"
        )

        await message.edit(f'✅Голосоое сообщение с именем "{text}"\nуспешно удалено.')
    except:
        logger.opt(colors=True).error(
            f"<red>Ошибка при использовании '-гс' в чате: {message.chat.id}</red>"
        )

        await message.edit(f'⚠️У вас нет голосового сообщения с именем "{text}".')