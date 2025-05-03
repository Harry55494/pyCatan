import random

from src.board.tile import Tile
from src.controller.events import GameEvent
from src.utils.logging import get_logger


class BoardModel:

    def __init__(self, events_manager, setup_method="default"):
        """
        Initialises a board object
        """

        # Set up the logger
        self.logger = get_logger("Board")
        self.logger.debug("Initialising board")
        self.event_manager = events_manager

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

    def change_random_tile(self):
        """
        Changes a random tile to a desert tile
        :return: None
        """
        self.logger.debug("Changing random tile to random other tile")
        # Get a random tile
        random_tile = random.choice(self.tiles)
        # Get a random resource
        random_resource = random.choice(self.box_tiles)
        # Get a random number
        random_number = random.choice(self.box_numbers)

        # Change the tile
        random_tile.resource = random_resource
        random_tile.dice_number = random_number
        random_tile.contains_robber = False

        # Dispatch the event
        self.event_manager.dispatch(
            GameEvent.TILE_CHANGED,
            {
                "tile": random_tile,
                "resource": random_resource,
                "dice_number": random_number,
            },
        )

    def move_piece(self):
        print("Moving piece")
        self.event_manager.dispatch(
            GameEvent.TILE_CHANGED, {"piece": "Knight", "position": (1, 2)}
        )
