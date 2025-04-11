from walk import MovePiece


class Flinger(MovePiece):
    def __init__(self, move_func, start_coord, curr_board):
        super().__init__(move_func, start_coord, curr_board)
        self.can_capture = False
        self.move_list = ["forward", "backward", "left", "right", "diagonal_left1", "diagonal_left2", "diagonal_right1",
                          "diagonal_right2"]
        self.fling_list = []
        self.action()

    def action(self):
        self.make_move(self.move_list)
        self.catapult(self.move_list)

    def catapult(self, move_list):
        self.check_fling_list(move_list)
        if self.fling_list:
            for piece in self.fling_list:
                self.fling(piece[0], piece[1]) # piece == (new coord, direction to fling)

    def fling(self, piece_coord, move):
        can_still_move = True
        this_coord = self.start_coord

        while can_still_move:
            this_coord = self.get_space(move, this_coord)
            can_still_move = self.in_da_air(this_coord, piece_coord)

    def in_da_air(self, new_coordinates, og_coordinates):
        if not self.out_of_bounds(new_coordinates):
            captured_piece = self.capture(new_coordinates)
            same_team = self.same_team(new_coordinates)
            king = False
            if captured_piece:
                king = self.curr_board[new_coordinates][1] == 'K'

            # ensures flinger cannot capture king
            if ((captured_piece and not same_team) or not captured_piece) and not king:
                move_info = (new_coordinates, captured_piece, og_coordinates)
                self.new_coords.append(move_info)
            return True
        return False

    def check_fling_list(self, move_list):
        for move in move_list:
            piece = self.get_space(move, self.start_coord)
            if not self.out_of_bounds(piece) and self.same_team(piece):
                self.fling_list.append((piece, self.get_opp_move(move)))

    def get_opp_move(self, move):
        if move == "forward":
            return "backward"
        if move == "backward":
            return "forward"
        if move == "left":
            return "right"
        if move == "right":
            return "left"
        if move == "diagonal_left1":
            return "diagonal_right2"
        if move == "diagonal_left2":
            return "diagonal_right1"
        if move == "diagonal_right1":
            return "diagonal_left2"
        if move == "diagonal_right2":
            return "diagonal_left1"

    def add_move(self, new_coordinates, move_until=False):
        if not self.out_of_bounds(new_coordinates):
            captured_piece = self.capture(new_coordinates)
            same_team = self.same_team(new_coordinates)
            # if can capture, deal with captured piece normally, piece can move anywhere
            # if cant capture, check if there is a piece in new coordinate, if so then dont append
            if (self.can_capture and not same_team) or (not self.can_capture and not captured_piece):
                move_info = (new_coordinates, captured_piece, None)
                self.new_coords.append(move_info)

            if move_until and captured_piece:
                return False
            return True