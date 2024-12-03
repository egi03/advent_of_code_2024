with open("input.txt") as f:
    inp = f.read()


import re

print(sum(map(lambda x: int(x[0]) * int(x[1]), [(x[4:len(x)-1]).split(",") for x in re.findall(r'mul\(\d+,\d+\)', inp)])))