import random

import dearpygui.dearpygui as dpg

import src.ui.view
from src.mvc.events import EventManager, GameEvent
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

    def setup(self):
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
        self.logger.debug("Running game")

        while dpg.is_dearpygui_running():

            if random.random() < 0.1:
                new_tile = random.choice(self.model.box_tiles)
                self.events_manager.dispatch(GameEvent.TILE_CHANGED, new_tile)

            dpg.render_dearpygui_frame()
