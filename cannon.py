from walk import MovePiece


class Cannon(MovePiece):
    def __init__(self, move_func, start_coord, curr_board):
        super().__init__(move_func, start_coord, curr_board)
        self.can_capture = False
        self.move_list = ["forward", "backward", "left", "right"]
        self.fire_list = ["diagonal_left1", "diagonal_left2", "diagonal_right1", "diagonal_right2"]
        self.destroy_list = []
        self.action()


    def action(self):
        self.make_move(self.move_list)
        self.fire()

    def fire(self):
        self.move_until(self.fire_list)

    # move_until is modified for the cannon
    # only adds a piece if its in the cannons firing range, no piece means no shot was taken
    def move_until(self, move_list):

        for move in move_list:
            can_still_move = True
            this_coord = self.start_coord

            move_info = []
            while can_still_move:
                this_coord = self.get_space(move, this_coord)
                can_still_move = self.check_firing_range(this_coord, move_info)
            if move_info:
                self.new_coords.append(tuple(move_info))

    def check_firing_range(self, new_coordinates, move_info):
        if not self.out_of_bounds(new_coordinates):
            captured_piece = self.capture(new_coordinates)

            if captured_piece:
                if not move_info:
                    move_info.append(None)
                if True not in move_info:
                    move_info.append(True)
                move_info.append(new_coordinates)
            return True
        return False

