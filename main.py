from src.game.board import Board
from src.ui.board_view import BoardView
from src.utils.info import get_version_display, get_ascii_title, get_repo_info
from src.utils.logging import get_logger

logger = get_logger("main")

logger.debug("Starting pyCatan")

ascii_title = get_ascii_title()
logger.info(ascii_title)
logger.info(f"{get_version_display()} - {get_repo_info()}\n")

logger.debug("Performing initialisation")

board = Board()

board_view = BoardView(board)

logger.debug("Initialisation complete, ready to run")

board_view.run()

logger.info("Game finished")
