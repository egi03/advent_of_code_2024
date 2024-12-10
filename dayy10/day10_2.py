def check_up(grid, x, y, v):
    if x - 1 >= 0 and grid[x - 1][y] == v + 1:
        return (x - 1, y, v + 1)
    return None

def check_down(grid, x, y, v):
    if x + 1 < len(grid) and grid[x + 1][y] == v + 1:
        return (x + 1, y, v + 1)
    return None

def check_left(grid, x, y, v):
    if y - 1 >= 0 and grid[x][y - 1] == v + 1:
        return (x, y - 1, v + 1)
    return None

def check_right(grid, x, y, v):
    if y + 1 < len(grid[0]) and grid[x][y + 1] == v + 1:
        return (x, y + 1, v + 1)
    return None

def calculate_score(grid, start):
    x, y, _ = start
    to_check = [(x, y, 0)]
    reachable_nines = set()

    while to_check:
        current = to_check.pop(0)

        cx, cy, cv = current
        if cv == 9:
            reachable_nines.add(len(to_check))
            continue

        for next_step in (check_up(grid, cx, cy, cv),
                          check_down(grid, cx, cy, cv),
                          check_left(grid, cx, cy, cv),
                          check_right(grid, cx, cy, cv)):
            if next_step:
                to_check.append(next_step)

    return len(reachable_nines)

with open("dayy10/input.txt") as f:
    grid = [[x for x in line.strip()] for line in f.read().splitlines()]


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            grid[i][j] = 300
        else:
            grid[i][j] = int(grid[i][j])


candidates = [(r, c, 0) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]

print(sum([calculate_score(grid, th) for th in candidates]))