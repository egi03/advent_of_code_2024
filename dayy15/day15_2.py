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
    double_grid = []
    for row in grid:
        doubled_row = []
        for c in row:
            if c == '@':
                doubled_row.append('@')
                doubled_row.append('.')
            elif c == 'O':
                doubled_row.append('[')
                doubled_row.append(']')
            else:
                doubled_row.append(c)
                doubled_row.append(c)
                
        double_grid.append(doubled_row)
    return double_grid, moves



grid, moves = parse_input("dayy15/input.txt")

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            break
    else:
        continue
    break

for move in moves:
    dr = {"^": -1, "v": 1}.get(move, 0)
    dc = {"<": -1, ">": 1}.get(move, 0)
    targets = [(r, c)]
    go = True
    for cr, cc in targets:
        nr = cr + dr
        nc = cc + dc
        if (nr, nc) in targets: continue
        char = grid[nr][nc]
        if char == "#":
            go = False
            break
        if char == "[":
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        if char == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))
    if not go: continue
    copy = [list(row) for row in grid]
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        grid[br][bc] = "."
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = copy[br][bc]
    r += dr
    c += dc

print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "["))