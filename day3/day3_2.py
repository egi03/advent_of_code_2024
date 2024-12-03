with open("input.txt") as f:
    inp = f.read()


import re

all_valid = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", inp)

total = 0
enabled = True

for x in all_valid:
    if enabled and x[0] == 'm':
        x = x[4:len(x)-1]
        first, second = x.split (",")
        total += int(first) * int(second)
    elif x[0] != 'm':
        enabled = x == "do()"


print(total)