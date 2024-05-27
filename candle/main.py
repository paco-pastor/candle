import logging

from config import Config
from termcolor import colored


class CustomFormatter(logging.Formatter):
    format = "%(asctime)s %(name)s %(message)s (%(filename)s)"

    FORMATS = {
        logging.DEBUG: colored(format, "green"),
        logging.INFO: colored(format, "white"),
        logging.WARNING: colored(format, "yellow"),
        logging.ERROR: colored(format, "red"),
        logging.CRITICAL: colored(format, "red", attrs=["bold"]),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        formatter.datefmt = "%m/%d/%y %I:%M:%S"
        return formatter.format(record)


class Candle(logging.Logger):
    console_handler = logging.StreamHandler()
    config = Config()

    def __init__(self, app="APP", level=logging.INFO):
        super().__init__(app)
        self.setLevel(level)
        self.console_handler.setLevel(level)
        self.console_handler.setFormatter(CustomFormatter())
        self.addHandler(self.console_handler)
        self.emojis = self.config.get_emojis()

    def format(self, level, msg):
        return f"{self.emojis[level]} {msg} "

    def debug(self, msg):
        super().debug(self.format("debug", msg))

    def info(self, msg):
        super().info(self.format("info", msg))

    def warning(self, msg):
        super().warning(self.format("warning", msg))

    def error(self, msg):
        super().error(self.format("error", msg))

    def critical(self, msg):
        super().critical(self.format("critical", msg))


log = Candle(level=logging.DEBUG)

log.debug("debug message")
log.info("info message")
log.warning("warning message")
log.error("error message")
log.critical("critical message")
