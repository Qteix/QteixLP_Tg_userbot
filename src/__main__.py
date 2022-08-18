from src.misc import app
from loguru import logger
import sys
from src.config import version


logger.remove()

logger.add(sys.stdout,
           format=f"[<yellow>Qteix LP {version}</yellow>]" + " <cyan>{"
                                                          "message}</cyan> [{time:HH:mm:ss}]",
           level="INFO")

logger.opt(colors=True).info(
            "Бот успешно запущен!"
        )

app.run()