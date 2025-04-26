import logging
import os
from datetime import datetime

class LoggerSetup:
    _instance = None
    _existing_loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSetup, cls).__new__(cls)
            cls._instance._setup_logging()
        return cls._instance

    def _setup_logging(self):
        os.makedirs("logs", exist_ok=True)

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        # Create a file handler
        log_file = os.path.join("logs", f"{datetime.now().strftime('%Y-%m-%d')}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        root_logger.addHandler(file_handler)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
        root_logger.addHandler(console_handler)
        self._existing_loggers = {
            "file": file_handler,
            "console": console_handler
        }


    def get_logger(self, name):
        if name not in self._existing_loggers:
            self._existing_loggers[name] = logging.getLogger(name)
        return self._existing_loggers[name]


def get_logger(name):
    return LoggerSetup().get_logger(name)
