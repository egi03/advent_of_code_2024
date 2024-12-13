def check_left(char, location, grid):
    r, c= location[0], location[1]
    if c-1 < 0 :
        return 0
    if grid[r][c-1] == char:
        return 1
    return 0

def check_right(char, location, grid):
    r, c= location[0], location[1]
    if c+1 >= len(grid[0]):
        return 0
    if grid[r][c+1] == char:
        return 1
    return 0

def check_up(char, location, grid):
    r, c= location[0], location[1]
    if r-1 < 0:
        return 0
    if grid[r-1][c] == char:
        return 1
    return 0

def check_down(char, location, grid):
    r, c= location[0], location[1]
    if r+1 >= len(grid):
        return 0
    if grid[r+1][c] == char:
        return 1
    return 0

def calculate_price(char, location, grid):
    # Returns every seen node, total price
    perimeter = 0
    area = 1
    to_check = [tuple(location)] # tuple is hashable
    seen = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while to_check:
        curr_location = to_check.pop()
        seen.add(curr_location)
        x, y = curr_location
        checks = [
            check_right(char, curr_location, grid),
            check_left(char, curr_location, grid),
            check_down(char, curr_location, grid),
            check_up(char, curr_location, grid)
        ]
        
        perimeter += (4 - sum(checks))
        for i, ch in enumerate(checks):
            new_loc = (x+directions[i][0], y+directions[i][1])
            if ch == 1 and new_loc not in seen and new_loc not in to_check:
                area += 1
                to_check.append(new_loc)
    return list(seen), area * perimeter





with open("dayy12/input.txt") as f:
    inp = [list(c) for c in list(f.read().splitlines())]



seen_nodes = set()
price = 0

for i, row in enumerate(inp):
    for j, char in enumerate(row):
        if (i, j) not in seen_nodes:
            new_seen, new_price = calculate_price(char, [i, j], inp)
            seen_nodes.update(new_seen)
            price += new_price

            
print(price)