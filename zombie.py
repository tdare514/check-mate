from walk import MovePiece


class Zombie(MovePiece):
    def __init__(self, move_func, start_coord, curr_board):
        super().__init__(move_func, start_coord, curr_board)
        # self.can_capture = False
        self.move_list = ["forward", "backward", "left", "right"]
        self.action()
        self.contagion_list = []

    def action(self):
        self.make_move(self.move_list)

    def check_contagion_list(self):
        for move in self.move_list:
            piece = self.get_space(move, self.start_coord)
            if not self.out_of_bounds(piece):
                captured_piece = self.capture(piece)
                same_team = self.same_team(piece)

                if captured_piece:
                    king = self.curr_board[piece][1] == 'K'
                    zombie = self.curr_board[piece][1] == 'Z'

                    if not same_team and not (king or zombie):
                        self.contagion_list.append(piece)

        return self.contagion_list
