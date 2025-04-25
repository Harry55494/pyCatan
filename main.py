import os
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

image_path = resource_path("assets/test_frog.png")
width, height, channels, data = dpg.load_image(image_path)

with dpg.texture_registry(show=True):
    dpg.add_static_texture(
        width=width, height=height, default_value=data, tag="512-mac"
    )

with dpg.theme() as transparent_theme:
    with dpg.theme_component(dpg.mvImageButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)


with dpg.window(
    label="game_window",
    width=800,
    height=550,
    no_close=True,
    no_collapse=True,
    no_resize=True,
    no_move=True,
    no_title_bar=True,
):
    dpg.add_text("Welcome to pyCatan!")
    dpg.add_image_button(
        label="test hex",
        width=100,
        height=100,
        texture_tag="512-mac",
        callback=lambda: print("test hex clicked"),
        tag="test_hex",
    )
    dpg.bind_item_theme("test_hex", transparent_theme)


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
