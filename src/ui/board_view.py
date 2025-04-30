import random

import dearpygui.dearpygui as dpg

from src.ui.command_processor import CommandProcessor
from src.utils.info import get_version_display, get_version
from src.utils.logging import get_logger
from src.utils.resources import resource_path


def print_tile_info(sender, app_data):
    """Print the tile info to the console."""
    tile_info = dpg.get_item_label(sender)
    print(f"Tile info: {tile_info}")


class BoardView:
    def __init__(self, game_state):
        self.logger = get_logger("BoardView")
        self.game_state = game_state
        self.logger.debug("Board view initialised")
        self.display_dimensions = (1200, 800)
        self.command_processor = CommandProcessor(game_state)

        self.touch_targets_vertices = [[250, 145], [200, 240]]
        self.touch_targets_vertices_active = False

        self.touch_targets_hexes = []

        dpg.create_context()

        dpg.create_viewport(
            title=get_version_display(),
            width=self.display_dimensions[0],
            height=self.display_dimensions[1],
            resizable=False,
        )

        with dpg.texture_registry(show=False):
            for tile_type in ["clay", "wheat", "forest", "sheep", "stone", "desert"]:
                # load the image
                image_path = resource_path(f"assets/game/tiles/{tile_type}.png")
                width, height, channels, data = dpg.load_image(image_path)

                # create a texture registry

                dpg.add_dynamic_texture(
                    width=width,
                    height=height,
                    default_value=data,
                    tag=f"{tile_type}-tile",
                )

            # load the board image
            image_path = resource_path("assets/game/board.png")
            width, height, channels, data = dpg.load_image(image_path)
            dpg.add_static_texture(
                width=width, height=height, default_value=data, tag="board"
            )

            image_path = resource_path("assets/game/tiles/tile_label.png")
            width, height, channels, data = dpg.load_image(image_path)
            dpg.add_static_texture(
                width=width, height=height, default_value=data, tag="tile_label"
            )

        with dpg.theme() as transparent_theme:
            with dpg.theme_component(dpg.mvImageButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 255, 255, 0])

        with dpg.font_registry():

            font_notoserif_variable_22 = dpg.add_font(
                resource_path("assets/fonts/NotoSerif-Variable.ttf"), 22
            )

            font_notoserif_variable_28 = dpg.add_font(
                resource_path("assets/fonts/NotoSerif-Variable.ttf"), 28
            )
            font_notoserif_variable_title = dpg.add_font(
                resource_path("assets/fonts/NotoSerif-Variable.ttf"), 50
            )

        with dpg.window(
            label="game_window",
            width=900,
            height=800,
            no_close=True,
            no_collapse=True,
            no_resize=True,
            no_move=True,
            no_title_bar=True,
            no_scrollbar=True,
            no_scroll_with_mouse=True,
            tag="game_window",
        ):
            dpg.add_image(
                tag="board2",
                texture_tag="board",
                width=900,
                height=800,
                pos=(0, 0),
            )

            board_tiles = self.game_state.tiles.copy()
            for row in range(5):

                offset_y = 125
                offset_x = 140 + (abs(row - 2) * 61)
                num_tiles = 5 if row == 2 else 4 if row == 1 or row == 3 else 3

                with dpg.group(horizontal=True):
                    for j in range(num_tiles):

                        placing_tile = board_tiles.pop(0)

                        tile_type = placing_tile.resource
                        tile_frequency = placing_tile.frequency

                        x, y = (offset_x + (122 * j), offset_y + (100 * row))

                        dpg.add_image(
                            label=f"test hex {row}{j}{tile_type}",
                            width=125,
                            height=133,
                            texture_tag=f"{tile_type}-tile",
                            tag=f"test_hex{row}{j}",
                            pos=(x, y),
                        )

                        dpg.bind_item_theme(f"test_hex{row}{j}", transparent_theme)

                        # also add the label in the center

                        if not placing_tile.dice_number == 7:

                            dpg.add_image(
                                texture_tag="tile_label",
                                width=35,
                                height=35,
                                pos=(x + 44, y + 48),
                                tag=f"text_bg{row}{j}",
                            )

                            dpg.add_text(
                                str(placing_tile.dice_number),
                                # Include offset for double digits
                                pos=(
                                    x
                                    + 52
                                    + (0 if placing_tile.dice_number >= 10 else 5),
                                    y + 48,
                                ),
                                tag=f"text_hex{row}{j}",
                                color=(
                                    (255, 0, 0)
                                    if placing_tile.dice_number in [6, 8]
                                    else (0, 0, 0)
                                ),
                            )

                            dpg.add_text(
                                "." * tile_frequency,
                                # Include offset for longer strings
                                pos=(x + 63 - (3 * tile_frequency), y + 50),
                                tag=f"dots_hex{row}{j}",
                                color=(
                                    (255, 0, 0)
                                    if placing_tile.dice_number in [6, 8]
                                    else (0, 0, 0)
                                ),
                            )

                            dpg.bind_item_font(
                                f"text_hex{row}{j}", font_notoserif_variable_22
                            )
                            dpg.bind_item_font(
                                f"dots_hex{row}{j}", font_notoserif_variable_28
                            )

            self.add_touch_targets_vertices()

        with dpg.window(
            label="title_window",
            width=300,
            height=200,
            no_close=True,
            no_collapse=True,
            no_resize=True,
            no_move=True,
            no_title_bar=True,
            pos=(900, 0),
        ):
            dpg.add_text(
                "pyCatan", pos=(80, 40), color=(255, 255, 255), tag="pyCatan_title"
            )
            dpg.add_text(
                "Version: " + get_version(),
                pos=(108, 105),
                color=(255, 255, 255),
                tag="pyCatan_version",
            )
            dpg.add_text(
                "github.com/Harry55494/pyCatan",
                pos=(50, 130),
                color=(255, 255, 255),
                tag="pyCatan_github",
            )
            dpg.bind_item_font("pyCatan_title", font_notoserif_variable_title)

        with dpg.window(
            label="Scoring and Game State",
            width=300,
            height=400,
            no_close=True,
            no_collapse=True,
            no_resize=True,
            no_move=True,
            no_title_bar=True,
            pos=(900, 200),
        ):
            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_text("")
                    dpg.add_text("Game State")

            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                for i in range(4):
                    with dpg.table_row():
                        dpg.add_text("")
                        dpg.add_text(f"Player {i + 1}")
                        dpg.add_text("Score: 0")

        with dpg.window(
            label="Command Window",
            width=300,
            height=200,
            no_close=True,
            no_collapse=True,
            no_resize=True,
            no_move=True,
            no_title_bar=True,
            pos=(900, 600),
        ):

            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_text("")
                    dpg.add_text("Command Input")

            dpg.add_input_text(label="", width=280, tag="command_input")
            dpg.add_button(label="Send", callback=self.process_command)
            dpg.add_button(
                label="Pause", callback=self.display_pause_menu, pos=(50, 58)
            )

        with dpg.handler_registry():
            dpg.add_key_release_handler(dpg.mvKey_Return, callback=self.process_command)
            dpg.add_key_release_handler(
                dpg.mvKey_Escape, callback=self.display_pause_menu
            )

        dpg.setup_dearpygui()
        dpg.set_exit_callback(lambda: dpg.stop_dearpygui())
        dpg.show_viewport()

    def display_pause_menu(self):
        width, height = 300, 200
        with dpg.window(
            label="Pause Menu",
            width=width,
            height=height,
            modal=True,
            tag="Pause Menu",
            no_move=True,
            pos=(
                self.display_dimensions[0] // 2 - (width / 2),
                self.display_dimensions[1] // 2 - (height / 2),
            ),
        ):
            dpg.add_button(
                label="Resume", callback=lambda: dpg.delete_item("Pause Menu")
            )
            dpg.add_button(label="Exit", callback=lambda: dpg.stop_dearpygui())

    def add_touch_targets_vertices(self):
        """
        Adds touch targets to the board
        """

        self.logger.debug("Adding vertex touch targets to the board")

        self.touch_targets_vertices_active = True

        def callback(sender, app_data):
            self.logger.debug(f"Touch target {sender} clicked")
            self.remove_touch_targets_vertices()
            self.touch_targets_vertices_active = False
            return sender

        for x, y in self.touch_targets_vertices:
            dpg.add_image_button(
                label=f"touch_target{x}{y}",
                width=30,
                height=30,
                texture_tag="tile_label",
                callback=callback,
                tag=f"touch_target{x}{y}",
                pos=(x, y),
                parent="game_window",
            )

    def remove_touch_targets_vertices(self):
        """
        Removes touch targets from the board
        """
        self.logger.debug("Removing vertex touch targets from the board")
        for x, y in self.touch_targets_vertices:
            dpg.delete_item(f"touch_target{x}{y}")

    def process_command(self):
        """
        Processes a command
        """
        command = dpg.get_value("command_input")
        self.command_processor.process_command(command)
        dpg.set_value("command_input", "")

    def run(self):

        self.logger.debug("Starting run loop")

        while dpg.is_dearpygui_running():

            if random.random() < 0.001 and not self.touch_targets_vertices_active:
                self.add_touch_targets_vertices()

            dpg.render_dearpygui_frame()

        self.logger.debug("Run loop exited")
