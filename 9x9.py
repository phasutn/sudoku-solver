def all_possible_state(table):
    possible_state = [[[] for _ in range(9)] for _ in range(9)]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != 0:
                possible_state[i][j] = 0
            else:
                for number in range(1, 10):
                    # Check row
                    if number not in table[i]:
                        # Check column
                        column_check = all(number != table[row][j] for row in range(len(table)))
                        if column_check:
                            # Check 3x3 grid
                            start_row = (i // 3) * 3
                            start_col = (j // 3) * 3
                            subgrid_check = all(number != table[row][col] for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3))
                            if subgrid_check:
                                possible_state[i][j].append(number)
    return possible_state

def single_state(possible_state, table):
    updated = False
    for row in range(len(possible_state)):
        for col in range(len(possible_state[row])):
            if possible_state[row][col] != 0:  
                if len(possible_state[row][col]) == 1:
                    table[row][col] = possible_state[row][col][0]
                    possible_state[row][col] = 0
                    updated = True
    return updated

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
    
    # Continuously update single states
    while single_state(possible_state, table):
        possible_state = all_possible_state(table)
    
    cell = select_cell(possible_state)
    if cell is None:
        return table  # Solution found
    
    for value in possible_state[cell[0]][cell[1]]:
        new_table = [row[:] for row in table]
        new_table[cell[0]][cell[1]] = value
        result = solve(new_table)
        if result:
            return result
    
    return None  # Backtrack

# Example usage for a 9x9 grid:
question = [
    [0, 1, 7, 8, 0, 0, 4, 0, 6],
    [0, 0, 0, 4, 0, 7, 0, 0, 2],
    [0, 0, 9, 0, 1, 0, 0, 7, 0],
    [5, 8, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 8, 7],
    [0, 9, 0, 0, 4, 0, 1, 0, 0],
    [1, 0, 0, 3, 0, 6, 0, 0, 0],
    [6, 0, 3, 0, 0, 9, 7, 2, 0]
]

solution = solve(question)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found")
