from walk import MovePiece


class Pawn(MovePiece):
    def __init__(self, move_func, start_coord, curr_board):
        super().__init__(move_func, start_coord, curr_board)
        self.can_capture = False
        self.move_list = ["forward"]
        self.action()

    def action(self):
        self.make_move(self.move_list)
        self.pawn_capture(["diagonal_left1", "diagonal_right1"])

    def pawn_capture(self, move_list):
        self.can_capture = True
        self.make_move(move_list)

    # doesnt require move_until but signatures need to be the same
    def add_move(self, new_coordinates, move_until=False):
        if not self.out_of_bounds(new_coordinates):
            captured_piece = self.capture(new_coordinates)
            same_team = self.same_team(new_coordinates)
            # if can capture, deal with captured piece normally,
                # pawns can only move diagonally if theres a piece to capture
            # if cant capture, check if there is a piece in new coordinate, if so then dont append
            if (self.can_capture and not same_team and captured_piece) or (not self.can_capture and not captured_piece):
                move_info = (new_coordinates, captured_piece)
                self.new_coords.append(move_info)
