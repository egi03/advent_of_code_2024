def rule_one(inp, index):
    if inp[index] == 0:
        inp[index] = 1
        return True
    return False

def rule_two(inp, index):
    num = inp[index]
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    length = len(digits)
    
    if length % 2 == 0:
        mid = length // 2
        first_half = int("".join(map(str, digits[:mid])))
        second_half = int("".join(map(str, digits[mid:])))
        inp[index] = first_half
        inp.insert(index + 1, second_half)
        return True
    return False

def rule_three(inp, index):
    inp[index] *= 2024
    return True

with open("input.txt") as f:
    inp = list(map(int, f.read().split()))

from tqdm import tqdm

for _ in tqdm(range(25)):
    ind = 0
    while ind < len(inp):
        if rule_one(inp, ind):
            ind += 1
        elif rule_two(inp, ind):
            ind += 2
        else:
            rule_three(inp, ind)
            ind += 1

print(len(inp))
