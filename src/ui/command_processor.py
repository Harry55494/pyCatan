from src.utils.logging import get_logger


class CommandProcessor:
    def __init__(self, game_state):
        """
        Initialises a command processor object
        """
        self.logger = get_logger("CommandProcessor")
        self.logger.debug("Initialising command processor")
        self.game_state = game_state

    def process_command(self, command):
        """
        Processes a command
        """
        self.logger.debug(f"Received command: {command}")
