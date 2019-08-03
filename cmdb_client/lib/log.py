import logging
from conf import settings


class Logger:
    def __init__(self, file_name, log_name, level=logging.INFO):
        file_handler = logging.FileHandler(file_name, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(message)s")
        file_handler.setFormatter(fmt)

        self.logger = logging.Logger(log_name, level=level)
        self.logger.addHandler(file_handler)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)


logger = Logger(settings.LOGGER_PATH, settings.LOGGER_NAME)
