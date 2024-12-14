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


def save_grid_as_image(robots, cell_size=50):
    width = COLS * cell_size
    height = ROWS * cell_size
    
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    
    for i in range(ROWS + 1):
        draw.line([(0, i * cell_size), (width, i * cell_size)], fill="black", width=1)
    for j in range(COLS + 1):
        draw.line([(j * cell_size, 0), (j * cell_size, height)], fill="black", width=1)
    
    for robot in robots:
        r, c = robot[0]
        x0, y0 = c * cell_size, r * cell_size
        x1, y1 = x0 + cell_size, y0 + cell_size
        draw.rectangle([x0, y0, x1, y1], fill="black")
    
    img.save(f"tree.png")


import re
from PIL import Image, ImageDraw

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

    for _ in range(7083):
        for robot in robots:
            robot[0] = move(robot[0], robot[1])

    save_grid_as_image(robots)


    mid_row = ROWS // 2
    mid_col = COLS // 2

    first_kv = len([r[0] for r in robots if r[0][0] < mid_row and r[0][1] < mid_col])
    second_kv = len([r[0] for r in robots if r[0][0] < mid_row and r[0][1] > mid_col])
    third_kv = len([r[0] for r in robots if r[0][0] > mid_row and r[0][1] < mid_col])
    fourth_kv = len([r[0] for r in robots if r[0][0] > mid_row and r[0][1] > mid_col])
    print(first_kv * second_kv * third_kv * fourth_kv)





if __name__ == "__main__":
    main()