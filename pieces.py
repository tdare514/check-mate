from walk import MoveBlack, MoveWhite
from flinger import Flinger
from knight import Knight
from peon import Peon
from king import King
from cannon import Cannon
from zombie import Zombie
from queen import Queen
from bishop import Bishop
from rook import Rook
class Pieces:
    def __init__(self, piece, start_coord, player_color, curr_board):
        self.new_coords = None
        self.contagion_list = None
        # determines which way pieces are moving
        if player_color == 'w':
            self.move_func = MoveWhite()
        else:
            self.move_func = MoveBlack()

        if piece == 'F':
            self.new_coords = Flinger(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'P':
            self.new_coords = Peon(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'N':
            self.new_coords = Knight(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'C':
            self.new_coords = Cannon(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'Q':
            self.new_coords = Queen(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'K':
            self.new_coords = King(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'Z':
            self.new_coords = Zombie(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'B':
            self.new_coords = Bishop(self.move_func, start_coord, curr_board).get_new_coords()

        elif piece == 'R':
            self.new_coords = Rook(self.move_func, start_coord, curr_board).get_new_coords()
        else:
            self.contagion_list = self.get_contagion_list(start_coord, curr_board)

    def get_contagion_list(self, start_coord, curr_board):
        return Zombie(self.move_func, start_coord, curr_board).check_contagion_list()
