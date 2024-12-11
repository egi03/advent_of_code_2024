dic = {} # (value, step): result

def calculate_total(value, step):
    if (value, step) in dic:
        return dic[(value, step)]
    
    if step == 0:
        return 1
    if value == 0:
        dic[(value, step)] = calculate_total(1, step-1)
        return calculate_total(1, step-1)
    length = len(str(value))
    
    if length % 2 == 0:
        mid = length // 2
        dic[(value, step)] = calculate_total(int(str(value)[mid:]), step-1) + calculate_total(int(str(value)[:mid]), step-1)
        return calculate_total(int(str(value)[mid:]), step-1) + calculate_total(int(str(value)[:mid]), step-1)
    
    dic[(value, step)] = calculate_total(value*2024, step-1)
    return calculate_total(value*2024, step-1)
    

import tqdm as tqdm


with open("dayy11/input.txt") as f:
    inp = list(map(int, f.read().split()))

total = 0
for x in tqdm.tqdm(inp):
    total += calculate_total(x, 75)

print(total)