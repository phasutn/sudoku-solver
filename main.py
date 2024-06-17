import numpy as np
import time

class sudoku:
    def __init__(self, board, row=0, col=0):
        self.board = board
        self.row = row
        self.col = col
        self.solved = False
    def all_filled(self):
        return np.all(self.board != 0)

    def placeable(self, row, col, num):
        if num in self.board[row]:
            return False
        elif num in self.board[:, col]:
            return False
        # Check the corresponding 3x3 grid for the number
        elif num in self.board[(row // 3) * 3:((row // 3) + 1) * 3, (col // 3) * 3:((col // 3) + 1) * 3]:
            return False
        else:
            return True

    def possible(self, row, col):
        buf = []
        for num in range(1, 10):
            if self.placeable(row, col, num):
                buf.append(num)
        if len(buf) > 0:
            return buf
        else:
            return 0

    def complete(self):
        # numpy.unique returns a sorted array of unique elements
        # numpy.arange creates an array of specified number
        # numpy.all does AND operation on the elements in the given array
        for i in range(9):
            # print(self.board[i, :])
            # print(np.arange(1, 10))
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

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row, col] != 0:
                    continue
                pos = self.possible(row, col)
                if pos == 0:
                    return None
                # print(f"First line: {self.board[0, :]}, row:{row} col:{col}")
                # print(pos)
                print(f"{self.board[row, :]}, row: {row}")
                for num in pos:
                    self.board[row, col] = num
                    if self.solve() is None:
                        self.board[row, col] = 0
                    elif self.solved:
                        return self.board
                if self.board[row, col] == 0:
                    return None
                    # new = np.copy(self.board)s
                    # new[row, col] = num
                    # new_sudoku = sudoku(new)
                    # result = new_sudoku.solve()
                    # if result is not None:
                    #     return result

        if self.all_filled() and self.complete():
            print("Solved")
            self.solved = True
            return self.board
        print("hello dog")


def main():
    start = time.time()

    print("test")
    board = np.array([
        [0, 0, 0, 1, 0, 0, 9, 2, 0],
        [0, 6, 0, 9, 0, 0, 8, 0, 0],
        [0, 1, 8, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 4],
        [0, 9, 4, 0, 3, 0, 6, 8, 0],
        [0, 8, 5, 0, 6, 0, 0, 1, 0],
        [1, 0, 9, 7, 0, 0, 0, 0, 0],
        [8, 7, 6, 0, 0, 0, 3, 4, 0],
        [5, 0, 0, 3, 0, 0, 0, 0, 0]
    ])

    new_board = sudoku(board)
    ans = new_board.solve()
    print(ans)

    end = time.time()
    print("Execution time:", (end - start) * 10 ** 3, "ms")
if __name__ == "__main__":
    main()
