import logging

class CustomFormatter(logging.Formatter):

    green = "\x1b[32;20m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s %(message)s (%(filename)s)"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        formatter.datefmt = "%m/%d/%y %I:%M:%S"
        return formatter.format(record)

class Candle(logging.Logger):
    console_handler = logging.StreamHandler()
    emoji_mapper = {
        "debug": "🐛",
        "info": "📰",
        "warning": "⚠️",
        "error": "🚨",
        "critical": "💥"
    }

    def __init__(self, app="LOGGER" ,level=logging.INFO, emoji_mapper={}):
        super().__init__(app)
        self.setLevel(level)
        self.console_handler.setLevel(level)
        self.console_handler.setFormatter(CustomFormatter())
        self.addHandler(self.console_handler)
        if emoji_mapper:
            self.emoji_mapper = emoji_mapper
    
    def format(self, level, msg, *args, **kwargs):
        return f"{self.emoji_mapper[level]} {msg} " + " ".join(args) + " " + " ".join(kwargs.values())

    def debug(self, msg, *args, **kwargs):
        super().debug(self.format("debug", msg, *args, **kwargs))
    
    def info(self, msg, *args, **kwargs):
        super().info(self.format("info", msg, *args, **kwargs))

    def warning(self, msg, *args, **kwargs):
        super().warning(self.format("warning", msg, *args, **kwargs))
    
    def error(self, msg, *args, **kwargs): # super is not called !!
        super().error(self.format("error", msg, *args, **kwargs))
    
    def critical(self, msg, *args, **kwargs):
        super().critical(self.format("critical", msg, *args, **kwargs))


log = Candle(level=logging.DEBUG)

log.debug("debug message", "hello", kwarg1="world")
log.info("info messaged")
log.warning("warning message")
log.error("error message")
log.critical("critical message")
