import math
import os
import random
import sys

import dearpygui.dearpygui as dpg


def print_message():
    """Print a message to the console."""
    print(f"Command: {dpg.get_value("command_input")}")
    dpg.set_value("command_input", "")
    # get the text from the input box


def exit_program():
    print("User has exited")


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


dpg.create_context()
dpg.create_viewport(title="pyCatan", width=800, height=800, resizable=False)

# create texture registry

with dpg.texture_registry(show=False):
    for tile_type in ["clay", "wheat", "forest", "sheep", "stone", "desert"]:
        # load the image
        image_path = resource_path(f"assets/game/tiles/{tile_type}.png")
        width, height, channels, data = dpg.load_image(image_path)

        # create a texture registry

        dpg.add_static_texture(
            width=width, height=height, default_value=data, tag=f"{tile_type}-tile"
        )

    # load the board image
    image_path = resource_path("assets/game/board.png")
    width, height, channels, data = dpg.load_image(image_path)
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="board")

with dpg.theme() as transparent_theme:
    with dpg.theme_component(dpg.mvImageButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 255, 255, 0])


def print_tile_info(sender, app_data):
    """Print the tile info to the console."""
    tile_info = dpg.get_item_label(sender)
    print(f"Tile info: {tile_info}")


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

    dpg.add_text("Welcome to pyCatan!")

    tiles = (
        []
        + 4 * ["wheat"]
        + 3 * ["clay"]
        + 3 * ["stone"]
        + 4 * ["sheep"]
        + 4 * ["forest"]
        + ["desert"]
    )
    random.shuffle(tiles)

    for row in range(5):

        offset_y = 70
        offset_x = 150 + (abs(row - 2) * 50)
        num_tiles = 5 if row == 2 else 4 if row == 1 or row == 3 else 3

        with dpg.group(horizontal=True):
            for j in range(num_tiles):

                tile_type = tiles.pop(0)

                x, y = (offset_x + (100 * j), offset_y + (78 * row))

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
    dpg.add_button(label="Exit", callback=lambda: dpg.stop_dearpygui(), pos=(750, 50))


with dpg.handler_registry():
    dpg.add_key_release_handler(dpg.mvKey_Return, callback=print_message)


dpg.setup_dearpygui()
dpg.set_exit_callback(exit_program)
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()
