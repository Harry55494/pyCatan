from src.game.board import Board
from src.ui.board_view import BoardView


# create texture registry

board = Board()

board_view = BoardView(board)

board_view.run()
