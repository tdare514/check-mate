from walk import MovePiece


class King(MovePiece):
    def __init__(self, move_func, start_coord, curr_board):
        super().__init__(move_func, start_coord, curr_board)
        # self.can_capture = False
        self.move_list = ["forward", "backward", "left", "right", "diagonal_left1", "diagonal_left2", "diagonal_right1", "diagonal_right2"]
        self.action()

    def action(self):
        self.make_move(self.move_list)

    # implement special moves
