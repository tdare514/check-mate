class BoardGame:
    def __init__(self):
        pass

    def print_row(self):
        print(" ", end="")
        for k in range(8):
            print("---", end=" ")
        print()
    def display_board(self):
        # print row letters
        self.print_row()
        for i in range(8):
            for j in range(8):
                if j == 0:
                    # print row num starting from 8
                    print("|", end="")
                print(" x |",  end="")
            print()
            # print row num starting from 8
            self.print_row()
        # print row letters
