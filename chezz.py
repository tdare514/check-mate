import pprint

from pieces import Pieces
import copy
import json


class Chezz:
    def __init__(self, board, line_one):
        self.state = board
        self.player_color = line_one[0]
        if self.player_color == 'w':
            self.next_player = 'b'
        if self.player_color == 'b':
            self.next_player = 'w'

        self.index_one, self.index_two, self.index_three = line_one[1:]
        self.coord_to_string = {
            (0, 7): 'a8', (1, 7): 'b8', (2, 7): 'c8', (3, 7): 'd8', (4, 7): 'e8', (5, 7): 'f8', (6, 7): 'g8', (7, 7): 'h8',
            (0, 6): 'a7', (1, 6): 'b7', (2, 6): 'c7', (3, 6): 'd7', (4, 6): 'e7', (5, 6): 'f7', (6, 6): 'g7', (7, 6): 'h7',
            (0, 5): 'a6', (1, 5): 'b6', (2, 5): 'c6', (3, 5): 'd6', (4, 5): 'e6', (5, 5): 'f6', (6, 5): 'g6', (7, 5): 'h6',
            (0, 4): 'a5', (1, 4): 'b5', (2, 4): 'c5', (3, 4): 'd5', (4, 4): 'e5', (5, 4): 'f5', (6, 4): 'g5', (7, 4): 'h5',
            (0, 3): 'a4', (1, 3): 'b4', (2, 3): 'c4', (3, 3): 'd4', (4, 3): 'e4', (5, 3): 'f4', (6, 3): 'g4', (7, 3): 'h4',
            (0, 2): 'a3', (1, 2): 'b3', (2, 2): 'c3', (3, 2): 'd3', (4, 2): 'e3', (5, 2): 'f3', (6, 2): 'g3', (7, 2): 'h3',
            (0, 1): 'a2', (1, 1): 'b2', (2, 1): 'c2', (3, 1): 'd2', (4, 1): 'e2', (5, 1): 'f2', (6, 1): 'g2', (7, 1): 'h2',
            (0, 0): 'a1', (1, 0): 'b1', (2, 0): 'c1', (3, 0): 'd1', (4, 0): 'e1', (5, 0): 'f1', (6, 0): 'g1', (7, 0): 'h1',
        }
        self.new_board_num = 0
        pass

    def edges(self):
        actions = self.get_possible_moves()

        for piece_type, all_pieces in actions.items():
            for piece, moves in all_pieces.items():
                move_list = moves["moves"]

                self.generate_board(piece, move_list, piece_type)

        # pprint.pprint(actions, sort_dicts=False)

    def generate_board(self, og_coord, move_list, piece_type):
        if not move_list:
            return
        for move in move_list:
            curr_board = copy.deepcopy(self.state)
            piece_info = curr_board[og_coord]
            new_spot = move[0]

            # make a regular move
            curr_board[og_coord] = ' '
            curr_board[new_spot] = piece_info

            self.promotion(curr_board)

            self.make_board_file(curr_board)

    def get_current_pieces(self):
        player_pieces = []
        for key, value in self.state.items():
            if value[0] == self.player_color:
                piece_position = (value[1], key)
                player_pieces.append(piece_position)
        return player_pieces

    def get_possible_moves(self):
        current_pieces = self.get_current_pieces()
        actions = {}
        # print(current_pieces)
        for piece_position in current_pieces:
            piece_type, piece_coords = piece_position
            # gets a list of moves this piece can make
            moves = self.evaluate_moves(piece_position)

            if piece_type not in actions:
                actions[piece_type] = {}
            # Store moves in a dictionary where the key is the piece's position
            actions[piece_type][piece_coords] = moves[piece_coords]

        return actions

    def evaluate_moves(self, piece_position):
        curr_board = copy.deepcopy(self.state)
        return {
            piece_position[1]: {
                "moves": Pieces(piece_position[0], piece_position[1], self.player_color, curr_board).new_coords}}

    def promotion(self, curr_board):
        peon_list = []
        for key, value in curr_board.items():
            if value[0] == self.player_color and value[1] == 'P':
                if self.end_of_board(key):
                    peon_list.append(key)

        if peon_list:
            for piece in peon_list:
                curr_board[piece] = f'{self.player_color}Q'

    def end_of_board(self, key):
        x, y = key
        if self.player_color == 'w':
            return y == 7
        elif self.player_color == 'b':
            return y == 0

    def make_board_file(self, curr_board):
        converted_board = {}
        for key, value in curr_board.items():
            if value != ' ':
                converted_board.update({self.coord_to_string[key]: value})

        board_file = open(f"board{self.new_board_num:03}.txt", "w")

        board_file.write(f"{self.next_player} {self.index_one} {self.index_two} {self.index_three}\n")

        board_file.write("{\n")
        for key, value in converted_board.items():
            board_file.write(f"  {key}: '{value}',\n")
        board_file.write("}\n")

        board_file.write("0\n0\n0\n")

        self.new_board_num += 1

    def print_board(self):
        for i, key in enumerate(self.state):
            if i % 8 == 0:
                print("")
            print(f"{key}:{self.state[key]}", end=" ")

        print("\n")
