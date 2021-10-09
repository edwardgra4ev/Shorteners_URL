from loguru import logger


logger.add("./log/error.log", format="{time} {level} {message}",
           level="ERROR", rotation="100 KB", compression="zip")

logger.add("./log/info.log", format="{time} {level} {message}",
           level="INFO", rotation="100 KB", compression="zip")