def all_possible_state(table):
    possible_state = [[[] for i in range(4)] for i in range(4)]                 
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != None:
                possible_state[i][j] = 0
            else:
                for number in range(1, 5):
                    # row
                    if number not in table[i]:
                        # colum
                        column_check = all(number != table[row][j] for row in range(len(table)))
                        if column_check:
                            # 2x2 grid
                            start_row = (i // 2) * 2
                            start_col = (j // 2) * 2
                            subgrid_check = all(number != table[row][col] for row in range(start_row, start_row + 2) for col in range(start_col, start_col + 2))
                            if subgrid_check:
                                possible_state[i][j].append(number)
    return possible_state

def single_state(possible_state, table):
    for row in range(len(possible_state)):
        for colum in range(len(possible_state[row])):
            if possible_state[row][colum] != 0:  
                if len(possible_state[row][colum]) == 1:
                    table[row][colum] = possible_state[row][colum][0]
                    possible_state[row][colum] = 0

def select_cell(possible_state):
    min_possibilities = float('inf')
    min_cell = None
    for i, row in enumerate(possible_state):
        for j, cell in enumerate(row):
            if cell != 0 and len(cell) < min_possibilities:
                min_possibilities = len(cell)
                min_cell = (i, j)
    return min_cell

def solve(table):
    possible_state = all_possible_state(table)
    single_state(possible_state, table)
    while True:
        while True:
            cell = select_cell(possible_state)
            if cell is None:
                return table  
    
# Example usage:
question = [
    [None, 3, 2, None],
    [None, 1, None, None],
    [None, None, 1, None],
    [None, 2, 3, None]
]

solution = solve(question)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")