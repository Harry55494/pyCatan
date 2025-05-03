import random

import dearpygui.dearpygui as dpg

import src.ui.view
from src.ui.view import render_frame
from src.controller.events import EventManager
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
        self.logger.debug("Running game")

        while dpg.is_dearpygui_running():

            # Game loop

            if random.random() < 0.005 and not self.view.touch_targets_vertices_active:
                # Simulate a game event

                self.view.add_touch_targets_vertices()

            render_frame()

        self.logger.debug("Game ended")
