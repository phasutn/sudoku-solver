import numpy as np


class sudoku:
    def __init__(self, board):
        self.board = board

    def placeable(self, row, col, num):
        if num in self.board[row]:
            return False
        elif num in self.board[:col]:
            return False
        # Check the corresponding 3x3 grid for the number
        elif num in self.board[(row // 3) * 3:((row // 3) + 1) * 3, (col // 3) * 3:((col // 3) + 1) * 3]:
            return False
        else:
            return True

    def possible(self, row, col):
        buf = []
        for num in range(1, 9):
            if self.placeable(row, col, num):
                buf.append(num)
        return buf

    def complete(self):
        # numpy.unique returns a sorted array of unique elements
        # numpy.arange creates an array of specified number
        # numpy.all does AND operation on the elements in the given array
        for i in range(9):
            if not np.all(np.unique(self.board[i, :]) == np.arange(1, 10)):
                return False
            if not np.all(np.unique(self.board[:, i]) == np.arange(1, 10)):
                return False
        # Check each 3x3 box for uniqueness
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not np.all(np.unique(self.board[row:row + 3, col:col + 3]) == np.arange(1, 10)):
                    return False
        return True


def main():
    print("test")
    board = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 1, 9, 5, 3, 4, 8],
        [0, 6, 8, 3, 4, 2, 5, 6, 7],
        [0, 5, 9, 7, 6, 1, 4, 2, 3],
        [0, 2, 6, 8, 5, 3, 7, 9, 1],
        [0, 1, 3, 9, 2, 4, 8, 5, 6],
        [0, 6, 1, 5, 3, 7, 2, 8, 4],
        [0, 6, 7, 4, 1, 9, 6, 3, 5],
        [0, 4, 5, 2, 8, 6, 1, 7, 9]
    ])


if __name__ == "__main__":
    main()
