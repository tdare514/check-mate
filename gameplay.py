class BoardGame:
    def __init__(self):
        self.x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.y_axis = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.board_list = []
        pass

    def print_row(self):
        print("      ", end="")
        for k in range(8):
            print("---", end=" ")
        print()

    def fill_board(self):
        # convert board to board list
        pass

    def print_x_axis(self):
        for i in range(8):
            print(f"  {self.x_axis[i]} ", end="")

    def print_y_axis(self, i):
        print(f"  {self.y_axis[i]}  ", end="")

    def display_board(self):
        print("     ", end="")
        self.print_x_axis()
        print()

        self.print_row()
        for i in range(8):
            for j in range(8):
                if j == 0:
                    self.print_y_axis(i)
                    print("|", end="")
                print(" x |", end="")
            self.print_y_axis(i)
            print()
            self.print_row()

        print("     ", end="")
        self.print_x_axis()
        print()

