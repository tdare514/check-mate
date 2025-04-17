from .walk import MovePiece


class Knight(MovePiece):
    def __init__(self, move_func, start_coord, curr_board):
        super().__init__(move_func, start_coord, curr_board)
        # self.can_capture = False
        self.move_list = [["forward", "forward", "left"],
                          ["forward", "forward", "right"],
                          ["forward", "left", "left"],
                          ["forward", "right", "right"],
                          ["backward", "backward", "left"],
                          ["backward", "backward", "right"],
                          ["backward", "left", "left"],
                          ["backward", "right", "right"]]
        self.action()

    def action(self):
        self.make_compound_move(self.move_list)
