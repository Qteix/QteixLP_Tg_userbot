from src.misc import app
from pyrogram import filters
from loguru import logger

"""

Отправка голосового сообщения

.гс <название гс>

"""

@app.on_message(filters.command('гс',prefixes='.') & filters.me)
async def gs_send(client,message):
    try:
        await app.delete_messages(chat_id=message.chat.id,message_ids=message.id)
        text = message.text.split('.гс ')[1]
        await app.send_voice(chat_id=message.chat.id,voice=f'gs/{text}.ogg',reply_to_message_id=message.reply_to_message_id)
        logger.opt(colors=True).info(
            f"<green>Использована комманда '.гс' в чате : {message.chat.id}</green>"
        )
    except:
        logger.opt(colors=True).error(
            f"<red>Ошибка при использовании '.гс' в чате: {message.chat.id}</red>"
        )
        await message.edit(f'⚠️Ошибка! Возможно у вас еще нету голосового шаблона с именем "{text}".')