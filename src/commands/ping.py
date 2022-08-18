from src.misc import app
from src.config import version
from pyrogram import filters
from loguru import logger
import random
import psutil
import platform
import time

"""
Показывает информацию о ОС

.пинг

"""

@app.on_message(filters.command('пинг',prefixes='.') & filters.me)
async def ping(client,message):

    logger.opt(colors=True).info(
            f"<green>Использована комманда 'пинг' в чате: {message.chat.id}</green>"
        )

    free = psutil.disk_usage('/').free/(1024*1024*1024)
    total = round(psutil.disk_usage('/').total/(1024*1024*1024))
    await message.edit(f"""

QteixLP | {version}
🖥 | Пинг: {round(random.random(),2)} сек
Информация о сервере:

📈 | Процесор: {round(psutil.cpu_percent())} %
⚙ | Оперативка: {round(psutil.virtual_memory()[3] / 2. ** 30, 2)} GB из {round(psutil.virtual_memory()[0] / 2. ** 30, 2)} GB
⏳ | Запущен: {round(time.perf_counter()//3600)} Часов
💿 | Disk: {free:.4} GB из {total} GB

Система: {platform.platform()}

""")
