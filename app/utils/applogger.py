from loguru import logger as mylogger

mylogger.add("app/logs/error_{time}.log", level="ERROR", format="{time} {level} {message}", rotation="12:00")