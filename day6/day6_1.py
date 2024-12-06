def move(inp, visited, location, direction_id):
    new_visited = visited.copy()

    while True:
        if direction_id == 0:  # Up
            temp_location = (location[0] - 1, location[1])
        elif direction_id == 1:  # Right
            temp_location = (location[0], location[1] + 1)
        elif direction_id == 2:  # Down
            temp_location = (location[0] + 1, location[1])
        elif direction_id == 3:  # Left
            temp_location = (location[0], location[1] - 1)

        # Check if it's done
        if not (0 <= temp_location[0] < len(inp) and 0 <= temp_location[1] < len(inp[0])):
            return len(new_visited)


        # Check if location will hit the wall
        if inp[temp_location[0]][temp_location[1]] == '#':
            break
        location = temp_location
        if location not in new_visited:
            new_visited.append(location)

    direction_id = direction_id + 1 if direction_id < 3 else 0
    return move(inp, new_visited, location, direction_id)


with open("input.txt") as f:
    inp = [x.strip() for x in f.readlines()]


start_location = ()
for i, l in enumerate(inp):
    if '^' in l:
        start_location = (i, l.index('^'))
        break

direction_id = 0
# 0 -> up, 1 -> right, 2 -> down, 3 -> left
visited = [start_location]
print(move(inp, visited, start_location, direction_id))
