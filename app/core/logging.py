import os
import sys

from loguru import logger

logger.remove()

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

logger.add(sys.stdout,
           level = "DEBUG",
           format = LOG_FORMAT,
           colorize=True,
           enqueue=False,
           backtrace=True,
           diagnose=True
           )

LOG_FILE_PATH = os.path.join("logs", "app.log")

logger.add(
    LOG_FILE_PATH,
    level="INFO",
    format=LOG_FORMAT,
    rotation="1 week",
    compression="zip",
    backtrace=True,
    diagnose=True
)

