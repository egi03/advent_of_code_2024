ROWS = 103
COLS = 101
def move(position, velocity):
    r, c = position
    move_r, move_c = velocity

    new_position_r = r + move_r
    new_position_c = c + move_c

    new_position_r %= ROWS
    new_position_c %= COLS
    return [new_position_r, new_position_c]


import re
def main():
    with open('dayy14/input.txt') as f:
        inp = f.read().splitlines()

    robots = [] #pos, vel
    for pos in inp:
        p = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", pos)
        robots.append([
                [int(p.group(2)), int(p.group(1))],
                [int(p.group(4)), int(p.group(3))]
            ])

    for r in robots:
        for _ in range(100):
            r[0] = move(r[0],r[1])

    mid_row = ROWS // 2
    mid_col = COLS // 2

    first_kv = len([r[0] for r in robots if r[0][0] < mid_row and r[0][1] < mid_col])
    second_kv = len([r[0] for r in robots if r[0][0] < mid_row and r[0][1] > mid_col])
    third_kv = len([r[0] for r in robots if r[0][0] > mid_row and r[0][1] < mid_col])
    fourth_kv = len([r[0] for r in robots if r[0][0] > mid_row and r[0][1] > mid_col])
    print(first_kv * second_kv * third_kv * fourth_kv)





if __name__ == "__main__":
    main()