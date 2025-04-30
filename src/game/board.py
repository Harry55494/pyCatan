import random

from src.game.tile import Tile
from src.utils.logging import get_logger


class Board:

    def __init__(self, setup_method="default"):
        """
        Initialises a board object
        """

        # Set up the logger
        self.logger = get_logger("Board")
        self.logger.debug("Initialising board")

        self.tiles = []

        # Save the tiles and numbers in order, can be randomised later

        self.box_tiles = [
            "stone",
            "sheep",
            "forest",
            "wheat",
            "clay",
            "sheep",
            "clay",
            "wheat",
            "forest",
            "desert",
            "forest",
            "stone",
            "forest",
            "stone",
            "wheat",
            "sheep",
            "clay",
            "wheat",
            "sheep",
        ]

        self.box_numbers = [
            10,
            2,
            9,
            12,
            6,
            4,
            10,
            9,
            11,
            3,
            8,
            8,
            3,
            4,
            5,
            5,
            6,
            11,
        ]

        self.logger.debug(f"Using {setup_method} board layout")

        if setup_method == "random":
            self.logger.debug("Randomising board layout")
            # Randomise the tiles and numbers
            random.shuffle(self.box_tiles)
            random.shuffle(self.box_numbers)

        for i in range(len(self.box_tiles)):

            if self.box_tiles[i] == "desert":
                # insert a 7
                self.box_numbers.insert(i, 7)

            self.tiles.append(
                Tile(
                    x=0,
                    y=0,
                    resource=self.box_tiles[i],
                    dice_number=self.box_numbers[i],
                    texture="",
                )
            )
