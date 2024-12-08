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
        for j in range(i + 1, len(array)):
            x_a, y_a = array[i]
            x_b, y_b = array[j]
            placed_antinode.add((2 * x_a - x_b, 2 * y_a - y_b))
            placed_antinode.add((2 * x_b - x_a, 2 * y_b - y_a))

print(len([0 for r, c in placed_antinode if 0 <= r < rows and 0 <= c < cols]))