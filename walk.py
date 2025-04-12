class BasicMove:
    def __init__(self, forward, backward, left, right):
        self.forward = forward
        self.backward = backward
        self.left = left
        self.right = right

    def move_forward(self, coordinates):
        x, y = coordinates
        new_coord = (x, y + self.forward)

        return new_coord

    def move_backward(self, coordinates):
        x, y = coordinates
        new_coord = (x, y + self.backward)

        return new_coord

    def move_left(self, coordinates):
        x, y = coordinates
        new_coord = (x + self.left, y)

        return new_coord

    def move_right(self, coordinates):
        x, y = coordinates
        new_coord = (x + self.right, y)

        return new_coord

    # direction can either be forward or backward
    def move_diagonal_left(self, coordinates, direction):
        temp_coord = self.move_left(coordinates)
        self.move_in(temp_coord, direction)

    def move_diagonal_right(self, coordinates, direction):
        temp_coord = self.move_right(coordinates)
        self.move_in(temp_coord, direction)

    def move_in(self, coord, direction):
        if direction == "forward":
            return self.move_forward(coord)
        elif direction == "backward":
            return self.move_backward(coord)


class MoveWhite(BasicMove):
    def __init__(self):
        super().__init__(forward=1, backward=-1, left=-1, right=1)


class MoveBlack(BasicMove):
    def __init__(self):
        super().__init__(forward=-1, backward=1, left=1, right=-1)


class MovePiece:
    def __init__(self, move_func, start_coord, curr_board):
        self.move_func = move_func
        self.start_coord = start_coord
        self.curr_board = curr_board

        self.can_capture = True
        # list of set of form (new_coordinates, captured) where captured is either none or location of a piece
        self.new_coords = []

    # gets coordinate of space in given direction from given coordinate
    def get_space(self, move, given_coord):
        this_coord = given_coord
        # expecting diagonals to indicate "diagonal_right1" for forward, "diagonal_left2" for backward
        if "1" in move:
            move_func = getattr(self.move_func, f"move_{move[:-1]}", None)
            this_coord = (move_func(this_coord, "forward"))
        elif "2" in move:
            move_func = getattr(self.move_func, f"move_{move[:-1]}", None)
            this_coord = (move_func(this_coord, "backward"))
        else:
            move_func = getattr(self.move_func, f"move_{move}", None)
            this_coord = (move_func(this_coord))

        return this_coord

    def make_move(self, move_list):
        for move in move_list:
            self.add_move(self.get_space(move, self.start_coord))

    def make_compound_move(self, move_list):
        for compound_move in move_list:
            this_coord = self.start_coord
            for move in compound_move:
                this_coord = self.get_space(move, this_coord)
            self.add_move(this_coord)

    # each move in the move_list is expected to go until either a piece is captured or theres no more room to move
    def move_until(self, move_list):
        for move in move_list:
            can_still_move = True
            this_coord = self.start_coord

            while can_still_move:
                this_coord = self.get_space(move, this_coord)
                can_still_move = self.add_move(this_coord, True)

    def add_move(self, new_coordinates, move_until=False):
        if not self.out_of_bounds(new_coordinates):
            captured_piece = self.capture(new_coordinates)
            same_team = self.same_team(new_coordinates)
            # if can capture, deal with captured piece normally, piece can move anywhere
            # if cant capture, check if there is a piece in new coordinate, if so then dont append
            if (self.can_capture and not same_team) or (not self.can_capture and not captured_piece):
                move_info = (new_coordinates, captured_piece)
                self.new_coords.append(move_info)

            if move_until and captured_piece:
                return False
            return True

    def out_of_bounds(self, coordinates):
        x, y = coordinates
        return x not in range(8) or y not in range(8)

    def capture(self, new_coordinates):
        # check if spot on board contains piece
        if self.curr_board[new_coordinates] != ' ':
            return True
        return False  # returns False if space is blank and True otherwise

    def same_team(self, new_coordinates):
        new_color = self.curr_board[new_coordinates][0]
        old_color = self.curr_board[self.start_coord][0]
        return new_color == old_color

    def get_new_coords(self):
        return self.new_coords
