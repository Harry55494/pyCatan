import dearpygui.dearpygui as dpg
from random import randint as random

def random_colour():
    """Generate a random colour."""
    return (random(0, 255), random(0, 255), random(0, 255), 255)

dpg.create_context()
dpg.create_viewport(title='pyCatan', width=600, height=400, resizable=False)


with dpg.window(label="pyCatan", width=600, height=400, no_close=True, no_collapse=True, no_resize=True, no_move=True):
    dpg.add_text("Welcome to pyCatan!")
    dpg.add_button(label="Exit", callback=lambda: dpg.stop_dearpygui())



dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()
