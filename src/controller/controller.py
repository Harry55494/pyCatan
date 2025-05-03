import random

import dearpygui.dearpygui as dpg

import src.ui.view
from src.controller.events import EventManager, GameEvent
from src.ui.view import render_frame
from src.utils.logging import get_logger


class BoardController:

    def __init__(self, events_manager: EventManager):
        """
        Initialises a game object
        """
        # Set up the logger

        self.view = None
        self.model = None
        self.logger = get_logger("MVC-Controller")

        self.logger.debug("Performing initialisation")

        self.events_manager = events_manager

        self.logger.debug("Initialisation complete, ready to run")

    def set_model(self, model):
        """
        Set the model for the game
        """
        self.model = model
        self.logger.debug("Model set")

    def set_view(self, view: src.ui.view.BoardView):
        """
        Set the view for the game
        :param view:
        :return:
        """
        self.view = view
        self.logger.debug("View set")

    def initialise_game(self):
        """
        Set up the game
        :return:
        """
        self.logger.debug("Setting up game")
        self.view.setup_window(self.model)
        self.logger.debug("Game setup complete")

    def run(self):
        """
        Run the game
        :return:
        """
        self.logger.debug("Beginning run loop")

        while dpg.is_dearpygui_running():

            # Game loop

            if (
                random.random() < 0.01
                and not self.view.touch_targets_vertices_active
                and not self.view.touch_targets_hexes_active
            ):
                # Simulate a game event

                def change_random(chosen_target):
                    chosen_target = chosen_target.replace("touch_hex_", "")
                    self.model.change_tile(chosen_target)
                    self.events_manager.unsubscribe(
                        GameEvent.TOUCH_TARGET_CHOSEN, change_random
                    )

                self.events_manager.subscribe(
                    GameEvent.TOUCH_TARGET_CHOSEN, change_random
                )

                self.view.add_touch_targets("hex")

            render_frame()

        self.logger.debug("Game ended")
