from src.game.board import Board
from src.ui.board_view import BoardView
from src.utils.logging import get_logger

logger = get_logger("main")


# create texture registry

logger.info("Starting game")

board = Board()

board_view = BoardView(board)

board_view.run()

logger.info("Game finished")
