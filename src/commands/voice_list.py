from src.misc import app
from pyrogram import filters
from loguru import logger
import os

"""

Показывает сохраненные голосовые сообщения

.гсы

"""


@app.on_message(filters.command('гсы',prefixes='.') & filters.me)
async def gs_list(client,message):
    result_gs = os.listdir('gs')
    if result_gs == []:

        logger.opt(colors=True).error(
            f"<red>Ошибка при использовании '.гсы' в чате: {message.chat.id}</red>"
        )

        await message.edit('⚠️У вас нету гс-шабов :c')
    else:
        
        tex = "\n -".join(result_gs).replace('.ogg','')
        await message.edit(f'ℹСписок ваших гс-шабов : \n-{tex}')

        logger.opt(colors=True).info(
            f"<green>Использована комманда '-гс' в чате : {message.chat.id}</green>"
        )