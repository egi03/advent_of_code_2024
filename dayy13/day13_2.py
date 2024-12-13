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
    x_res = int(result.group(1)) + 10000000000000
    y_res = int(result.group(2)) + 10000000000000

    total_a = (x_res * y_b - y_res * x_b) / (x_a * y_b - y_a * x_b)
    total_b = (x_res - x_a * total_a) / x_b
    if total_a % 1 == total_b % 1 == 0:
        return int(total_a * 3 + total_b)
    return 0

def main():
    with open("dayy13/input.txt") as f:
        inp = [x for x in f.read().split('\n\n')]

    total_credits = 0
    for eq in inp:
        total_credits += generate_equation(eq)
    print(total_credits)

if __name__ == "__main__":
    main()