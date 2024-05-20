import numpy as np


def placeable(grid, row, col, num):
    if num in grid[row]:
        return False
    elif num in grid[:col]:
        return False
    # Check the corresponding 3x3 grid for the number
    elif num in grid[(row // 3) * 3:((row // 3) + 1) * 3, (col // 3) * 3:((col // 3) + 1) * 3]:
        return False
    else:
        return True

def possible(grid, row, col):
    list = []
    for num in range(1,10):
        if num not in grid[row, :] and num not in grid[:, col] and num not in grid[(row // 3) * 3:((row // 3) + 1) * 3, (col // 3) * 3:((col // 3) + 1) * 3]:
            list.append(num)
    return list
def complete(grid):
    # numpy.unique returns a sorted array of unique elements
    # numpy.arange creates an array of specified number
    # numpy.all does AND operation on the elements in the given array
    for i in range(9):
        if not np.all(np.unique(grid[i, :]) == np.arange(1, 10)):
            return False
        if not np.all(np.unique(grid[:, i]) == np.arange(1, 10)):
            return False
    #Check each 3x3 box for uniqueness
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not np.all(np.unique(grid[row:row + 3, col:col + 3]) == np.arange(1, 10)):
                return False
    return True


def main():
    print("test")
    grid = np.array([
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
    # print(complete(grid))
    # for i in range(9):
    #     for j in range(9):
    #         print('test')
    print(possible(grid, 0, 0))


if __name__ == "__main__":
    main()
