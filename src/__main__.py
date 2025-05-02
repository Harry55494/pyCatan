from src.mvc.events import EventManager
from src.mvc.controller import BoardController
from src.board.model import BoardModel
from src.ui.view import BoardView
from src.utils.info import get_version_display, get_ascii_title, get_repo_info
from src.utils.logging import get_logger

logger = get_logger("main")

logger.debug("Starting pyCatan")

ascii_title = get_ascii_title()
logger.info(ascii_title)
logger.info(f"{get_version_display()} - {get_repo_info()}\n")

events_manager = EventManager()

board = BoardModel(events_manager)
view = BoardView(events_manager)
controller = BoardController(events_manager)

controller.set_model(board)
controller.set_view(view)
controller.setup()

controller.run()
