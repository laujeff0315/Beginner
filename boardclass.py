from random import randint

class Board(object):

    #initiate the board object:
    def __init__(self,board_size):
        self.board = [ ["()"] * board_size for x in range(board_size)]
        self.size = board_size

    def __str__(self):
        board_str = "Row"+"\n"
        a = self.size
        board = self.board
        n = 0
        if a > 1:
            for row in board:
                board_str = board_str + "%02d "%(n) + " ".join(row) + "\n"
                n += 1

            str_col = ["%02d"%(x) for x in list(range(a))]
            board_str = board_str + "   "+" ".join(str_col) +" Col"
            return board_str
        elif a == 1:
            return "0"

    def random_row(self):
        return randint(0, self.size - 1)

    def random_col(self):
        return randint(0, self.size - 1)