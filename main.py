import numpy as np


class sudoku:
    def __init__(self, board, row=0, col=0):
        self.board = board
        self.row = row
        self.col = col

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

    def solve(self, start_row=0, start_col=0):
        # print(f"entering row:{start_row} col:{start_col}")
        for row in range(start_row, 9):
            for col in range(start_col, 9):
                if self.board[row, col] == 0:
                    pos = self.possible(row, col)
                    print(f"possible values at {row}, {col} are {pos}")
                    # print(f"check1 {self.board[row, :]}")
                    # print(f"check2 {self.board[:, col]}")
                    if not pos:
                        return None
                    for num in pos:
                        new_board = np.copy(self.board)
                        new_board[row, col] = num
                        solved_board = sudoku(new_board).solve(row, col)
                        if solved_board is not None:
                            return solved_board  # Return the solution
        if self.all_filled() and self.complete():
            print("Solved")
            return self.board
        return None

def main():
    print("test")
    board = np.array([
        [5, 2, 0, 0, 0, 0, 0, 8, 1],
        [0, 3, 9, 5, 8, 0, 0, 0, 0],
        [0, 8, 0, 0, 9, 0, 0, 0, 0],
        [2, 4, 0, 0, 0, 0, 1, 0, 3],
        [1, 0, 0, 4, 3, 0, 8, 6, 0],
        [0, 6, 3, 0, 0, 7, 0, 2, 4],
        [0, 0, 0, 1, 0, 9, 3, 5, 0],
        [0, 0, 8, 0, 7, 4, 6, 0, 0],
        [3, 1, 0, 8, 6, 0, 7, 0, 9]
    ])

    new_board = sudoku(board)
    ans = new_board.solve()
    print(ans)

if __name__ == "__main__":
    main()
