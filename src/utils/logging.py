import logging
import os
import sys
from datetime import datetime

import appdirs

TERMINAL_LOGGING_LEVEL = logging.DEBUG
FILE_LOGGING_LEVEL = logging.DEBUG


class LoggerSetup:
    _instance = None
    _existing_loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSetup, cls).__new__(cls)
            cls._instance._setup_logging()
        return cls._instance

    def _setup_logging(self):

        try:
            sys._MEIPASS
            log_dir = os.path.join(
                appdirs.user_log_dir("pyCatan", "com.phillingham"), "logs"
            )
        except Exception:
            base_path = os.path.abspath("")
            log_dir = os.path.join(base_path, "logs")

        os.makedirs(log_dir, exist_ok=True)

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        # Create a file handler
        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(FILE_LOGGING_LEVEL)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        root_logger.addHandler(file_handler)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(TERMINAL_LOGGING_LEVEL)
        console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
        root_logger.addHandler(console_handler)

        # Store handlers separately from loggers
        self._handlers = {"file": file_handler, "console": console_handler}
        self._existing_loggers = {}

    def get_logger(self, name):
        if name not in self._existing_loggers:
            self._existing_loggers[name] = logging.getLogger(name)
        return self._existing_loggers[name]


def get_logger(name):
    return LoggerSetup().get_logger(name)
