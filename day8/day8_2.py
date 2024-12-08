with open("day8/input.txt") as f:
    inp = f.read().splitlines()

rows = len(inp)
cols = len(inp[0])

antennas = {}

for r, row in enumerate(inp):
    for c, char in enumerate(row):
        if char != ".":
            if char not in antennas: antennas[char] = []
            antennas[char].append((r, c))

placed_antinode = set()

for array in antennas.values():
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j: 
                continue
            x_a, y_a = array[i]
            x_b, y_b = array[j]
            
            change_x = x_b - x_a
            change_y = y_b - y_a
            r = x_a
            c = y_a
            while 0 <= r < rows and 0 <= c < cols:
                placed_antinode.add((r, c))
                r += change_x
                c += change_y


print(len(placed_antinode))