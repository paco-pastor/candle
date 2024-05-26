import logging

from config import Config


class CustomFormatter(logging.Formatter):

    green = "\x1b[32;20m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s %(name)s %(message)s (%(filename)s)"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
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
