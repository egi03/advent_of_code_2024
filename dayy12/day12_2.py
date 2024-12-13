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
        
        for i, ch in enumerate(checks):
            new_loc = (x+directions[i][0], y+directions[i][1])
            if ch == 1 and new_loc not in seen and new_loc not in to_check:
                area += 1
                to_check.append(new_loc)
    
    total_price = get_sides(seen)
    return list(seen), area * total_price

def get_sides(seen):
    corner_candidates = set()
    for r, c in seen:
        for corn_row, corn_col in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((corn_row, corn_col))
    corners = 0
    for corn_row, corn_col in corner_candidates:
        config = [(sr, sc) in seen for sr, sc in [(corn_row - 0.5, corn_col - 0.5), (corn_row + 0.5, corn_col - 0.5), (corn_row + 0.5, corn_col + 0.5), (corn_row - 0.5, corn_col + 0.5)]]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners



def main():
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
    
if __name__ == "__main__":
    main()