with open("input.txt") as f:
    inp = f.read()


import re

all_valid = re.findall(r'mul\(\d+,\d+\)', inp)

total = 0

for x in all_valid:
    x = x[4:len(x)-1]
    first, second = x.split (",")
    total += int(first) * int(second)


print(total)