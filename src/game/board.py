import random

from src.utils.logging import get_logger


class Board:

    def __init__(self):
        """
        Initialises a board object
        """

        # Set up the logger
        self.logger = get_logger("Board")
        self.logger.debug("Initialising board")

        self.tiles = (
            []
            + 4 * ["wheat"]
            + 3 * ["clay"]
            + 3 * ["stone"]
            + 4 * ["sheep"]
            + 4 * ["forest"]
            + ["desert"]
        )
        random.shuffle(self.tiles)
