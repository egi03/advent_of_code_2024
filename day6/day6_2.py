def is_in_loop(inp, row, col):
    # -1 ide gore/lijevo, 1 ide dolje/desno
    row_change = -1
    col_change = 0

    visited = set()

    while True:
        visited.add((row,col,row_change,col_change))
        if row+row_change < 0 or row+row_change >= rows or col + col_change < 0 or col + col_change >= cols:
            return False
        if inp[row + row_change][col+col_change] == '#':
            # Turn right
            row_change, col_change = col_change, -row_change
        else:
            row += row_change
            col += col_change


        if(row, col, row_change, col_change) in visited:
            return True


with open("input.txt") as f:
    inp = [list(x) for x in f.read().splitlines()]

rows = len(inp)
cols = len(inp[0])

for i, l in enumerate(inp):
    if '^' in l:
        start_row, start_col = i, l.index('^')
        break

total = 0

for r in range(rows):
    for c in range(cols):
        if inp[r][c] == '.':
            inp[r][c] = '#'
            if is_in_loop(inp,start_row,start_col):
                total += 1
            inp[r][c] = '.'

print(total)