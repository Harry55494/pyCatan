from src.board.model import BoardModel
from src.board.state import GameState
from src.controller.controller import BoardController
from src.controller.events import EventManager
from src.ui.view import BoardView
from src.utils.info import get_version_display, get_ascii_title, get_repo_info
from src.utils.logging import get_logger

if __name__ == "__main__":

    logger = get_logger("main")

    logger.info("Starting pyCatan")

    ascii_title = get_ascii_title()
    logger.info(ascii_title)
    logger.info(f"{get_version_display()} - {get_repo_info()}\n")

    events_manager = EventManager()

    board = BoardModel(events_manager)
    view = BoardView(events_manager)
    controller = BoardController(events_manager)
    state = GameState(events_manager)

    controller.set_model(board)
    controller.set_view(view)
    controller.set_state(state)
    controller.initialise_game()

    controller.run()
