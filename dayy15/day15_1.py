def move_up(position, grid):
    r, c = position
    wanted_row = r-1
    if grid[wanted_row][c] == '.':
        grid[r][c] = '.'
        grid[wanted_row][c] = '@'
    if grid[wanted_row][c] == 'O':
        new_r = wanted_row
        while grid[new_r][c] == 'O':
            new_r -= 1
        if grid[new_r][c] == '.':
            grid[new_r][c] = 'O'
            grid[wanted_row][c] = '@'
            grid[r][c] = '.'
    return grid

def move_down(position, grid):
    r, c = position
    wanted_row = r+1
    if grid[wanted_row][c] == '.':
        grid[r][c] = '.'
        grid[wanted_row][c] = '@'
    if grid[wanted_row][c] == 'O':
        new_r = r+1
        while grid[new_r][c] == 'O':
            new_r += 1
        if grid[new_r][c] == '.':
            grid[new_r][c] = 'O'
            grid[wanted_row][c] = '@'
            grid[r][c] = '.'
    return grid

def move_left(position, grid):
    r, c = position
    wanted_col = c-1
    if grid[r][wanted_col] == '.':
        grid[r][c] = '.'
        grid[r][wanted_col] = '@'
    if grid[r][wanted_col] == 'O':
        new_c = c-1
        while grid[r][new_c] == 'O':
            new_c -= 1
        if grid[r][new_c] == '.':
            grid[r][new_c] = 'O'
            grid[r][wanted_col] = '@'
            grid[r][c] = '.'
    return grid

def move_right(position, grid):
    r, c = position
    wanted_col = c+1
    if grid[r][wanted_col] == '.':
        grid[r][c] = '.'
        grid[r][wanted_col] = '@'
    if grid[r][wanted_col] == 'O':
        new_c = c+1
        while grid[r][new_c] == 'O':
            new_c += 1
        if grid[r][new_c] == '.':
            grid[r][new_c] = 'O'
            grid[r][wanted_col] = '@'
            grid[r][c] = '.'
    return grid

def find_at(grid):
    for row_index, row in enumerate(grid):
        if '@' in row:
            col_index = row.index('@')
            return [row_index, col_index]

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    grid = []
    moves = []
    grid_mode = True
    
    for line in lines:
        line = line.strip()
        if not line:
            grid_mode = False
        elif grid_mode:
            grid.append(list(line))
        else:
            moves.append(line)
    
    moves = ''.join(moves)
    return grid, moves


inp, moves = parse_input("dayy15/input.txt")

for m in moves:
    if m == '<':
        inp = move_left(find_at(inp), inp)
    elif m == '>':
        inp = move_right(find_at(inp), inp)
    elif m == '^':
        inp = move_up(find_at(inp), inp)
    elif m == 'v':
        inp = move_down(find_at(inp), inp)
    
total = 0

for r, row in enumerate(inp):
    for c, char in enumerate(row):
        if char == 'O':
            total += 100 * r + c
            
print(total)