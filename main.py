import dearpygui.dearpygui as dpg


def print_message():
    """Print a message to the console."""
    print(f"Command: {dpg.get_value("command_input")}")
    dpg.set_value("command_input", "")
    # get the text from the input box


def exit_program():
    print("User has exited")


dpg.create_context()
dpg.create_viewport(title="pyCatan", width=800, height=800, resizable=False)


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
    dpg.add_button(label="Exit", callback=lambda: dpg.stop_dearpygui())

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


with dpg.handler_registry():
    dpg.add_key_release_handler(dpg.mvKey_Return, callback=print_message)


dpg.setup_dearpygui()
dpg.set_exit_callback(exit_program)
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()
