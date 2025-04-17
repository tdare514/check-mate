from .walk import MoveBlack, MoveWhite
from .knight import Knight
from .pawn import Pawn
from .king import King
from .queen import Queen
from .bishop import Bishop
from .rook import Rook


class Pieces:
    def __init__(self, piece, start_coord, player_color, curr_board):
        self.new_coords = None

        if player_color == 'w':
            self.move_func = MoveWhite()
        else:
            self.move_func = MoveBlack()

        if piece == 'P':
            self.new_coords = Pawn(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'N':
            self.new_coords = Knight(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'Q':
            self.new_coords = Queen(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'K':
            self.new_coords = King(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'B':
            self.new_coords = Bishop(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'R':
            self.new_coords = Rook(self.move_func, start_coord, curr_board).get_new_coords()

        else:
            pass
