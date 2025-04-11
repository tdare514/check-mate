from walk import MovePiece


class Rook(MovePiece):
    def __init__(self, move_func, start_coord, curr_board):
        super().__init__(move_func, start_coord, curr_board)
        self.can_capture = True
        self.move_list = ["forward", "backward", "left", "right"]
        self.action()

    def action(self):
        self.move_until(self.move_list)
