import random

import dearpygui.dearpygui as dpg

from src.utils.logging import get_logger
from src.utils.resources import resource_path
from src.utils.get_version import get_version_display


def print_message():
    """Print a message to the console."""
    print(f"Command: {dpg.get_value("command_input")}")
    dpg.set_value("command_input", "")


def print_tile_info(sender, app_data):
    """Print the tile info to the console."""
    tile_info = dpg.get_item_label(sender)
    print(f"Tile info: {tile_info}")


class BoardView:
    def __init__(self, game_state):
        self.logger = get_logger("BoardView")
        self.game_state = game_state
        self.logger.debug("Board view initialised")
        self.display_dimensions = (800, 800)

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

        with dpg.theme() as transparent_theme:
            with dpg.theme_component(dpg.mvImageButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 255, 255, 0])

        with dpg.window(
            label="game_window",
            width=800,
            height=550,
            no_close=True,
            no_collapse=True,
            no_resize=True,
            no_move=True,
            no_title_bar=True,
            no_scrollbar=True,
            no_scroll_with_mouse=True,
        ):
            dpg.add_image(
                tag="board2",
                texture_tag="board",
                width=800,
                height=800,
                pos=(0, 0),
            )

            board_tiles = self.game_state.tiles
            for row in range(5):

                offset_y = 70
                offset_x = 150 + (abs(row - 2) * 50)
                num_tiles = 5 if row == 2 else 4 if row == 1 or row == 3 else 3

                with dpg.group(horizontal=True):
                    for j in range(num_tiles):
                        tile_type = board_tiles.pop(0)

                        x, y = (offset_x + (99 * j), offset_y + (77 * row))

                        dpg.add_image_button(
                            label=f"test hex {row}{j}{tile_type}",
                            width=100,
                            height=100,
                            texture_tag=f"{tile_type}-tile",
                            callback=print_tile_info,
                            tag=f"test_hex{row}{j}",
                            pos=(x, y),
                        )

                        dpg.bind_item_theme(f"test_hex{row}{j}", transparent_theme)

        with dpg.window(
            label="Scoring and Game State",
            width=800,
            height=150,
            no_close=True,
            no_collapse=True,
            no_resize=True,
            no_move=True,
            no_title_bar=True,
            pos=(0, 550),
        ):
            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_text("")
                    dpg.add_text("")
                    dpg.add_text("Game State")

                for i in range(4):
                    with dpg.table_row():
                        dpg.add_text("")
                        dpg.add_text(f"Player {i + 1}")
                        dpg.add_text("Score: 0")
                        dpg.add_text("Resources: 0")

        with dpg.window(
            label="Command Window",
            width=800,
            height=100,
            no_close=True,
            no_collapse=True,
            no_resize=True,
            no_move=True,
            pos=(0, 700),
        ):
            dpg.add_input_text(label="", width=780, tag="command_input")
            dpg.add_button(label="Send", callback=print_message)
            dpg.add_button(
                label="Pause", callback=self.display_pause_menu, pos=(745, 50)
            )

        with dpg.handler_registry():
            dpg.add_key_release_handler(dpg.mvKey_Return, callback=print_message)
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

    def run(self):
        while dpg.is_dearpygui_running():

            # choose a random hex based on tag

            if random.random() < 0.05:  # Adjust probability to control frequency
                # Get a random row and column
                row = random.randint(0, 4)
                # Determine max column for the selected row
                max_col = 4 if row == 2 else 3 if row == 1 or row == 3 else 2
                col = random.randint(0, max_col)

                # Valid tile tag
                tag = f"test_hex{row}{col}"

                # Get a random new tile type
                tile_types = ["clay", "wheat", "forest", "sheep", "stone", "desert"]
                new_tile_type = random.choice(tile_types)

                # Change the texture
                dpg.configure_item(tag, texture_tag=f"{new_tile_type}-tile")
                # Change the label
                dpg.set_item_label(tag, f"test hex {row}{col}{new_tile_type}")

                print(f"Changed {tag} to {new_tile_type}")

            dpg.render_dearpygui_frame()
