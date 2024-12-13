import numpy as np
import re

def generate_equation(eq):
    button_a = re.search(r"Button A: X\+(\d+), Y\+(\d+)", eq)
    button_b = re.search(r"Button B: X\+(\d+), Y\+(\d+)", eq)
    result = re.search(r"Prize: X=(\d+), Y=(\d+)", eq)
    x_a = int(button_a.group(1))
    y_a = int(button_a.group(2))
    x_b = int(button_b.group(1))
    y_b = int(button_b.group(2))
    x_res = int(result.group(1))
    y_res = int(result.group(2))

    E = np.array([[x_a, x_b], [y_a, y_b]])
    res = np.array([x_res, y_res])

    eq_res = np.linalg.solve(E, res)

    floating_error = 1e-12
    check_first = abs(eq_res[0] - round(eq_res[0])) < floating_error
    check_second = abs(eq_res[1] - round(eq_res[1])) < floating_error
    if check_first and check_second:
        return int(round(eq_res[0])), int(round(eq_res[1]))
    return 0, 0




def main():
    with open("dayy13/input.txt") as f:
        inp = [x for x in f.read().split('\n\n')]

    total_credits = 0
    for eq in inp:
        a, b= generate_equation(eq)
        total_credits += a*3
        total_credits += b*1
    print(total_credits)

if __name__ == "__main__":
    main()