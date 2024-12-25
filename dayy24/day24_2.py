with open("dayy24/input.txt") as f:
    formulas = {}

    for line in f:
        if line.isspace(): 
            break

    for line in f:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)

def create_wire(char, num):
    return char + str(num).rjust(2, "0")

def is_valid_z(wire, num):
    if wire not in formulas: 
        return False
    op, x, y = formulas[wire]
    if op != "XOR": 
        return False
    if num == 0: 
        return sorted([x, y]) == ["x00", "y00"]
    return is_valid_middle_cor(x, num) and is_valid_carry(y, num) or is_valid_middle_cor(y, num) and is_valid_carry(x, num)

def is_valid_middle_cor(wire, num):
    if wire not in formulas: 
        return False
    op, x, y = formulas[wire]
    if op != "XOR": 
        return False
    return sorted([x, y]) == [create_wire("x", num), create_wire("y", num)]

def is_valid_carry(wire, num):
    if wire not in formulas: 
        return False
    op, x, y = formulas[wire]
    if num == 1:
        if op != "AND": 
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR": 
        return False
    return is_valid_dcarry(x, num - 1) and is_valid_rcarry(y, num - 1) or is_valid_dcarry(y, num - 1) and is_valid_rcarry(x, num - 1)

def is_valid_dcarry(wire, num):
    if wire not in formulas: 
        return False
    op, x, y = formulas[wire]
    if op != "AND": 
        return False
    return sorted([x, y]) == [create_wire("x", num), create_wire("y", num)]

def is_valid_rcarry(wire, num):
    if wire not in formulas: 
        return False
    op, x, y = formulas[wire]
    if op != "AND": 
        return False
    return is_valid_middle_cor(x, num) and is_valid_carry(y, num) or is_valid_middle_cor(y, num) and is_valid_carry(x, num)

def verify(num):
    return is_valid_z(create_wire("z", num), num)

def progress():
    i = 0
    
    while True:
        if not verify(i): break
        i += 1
    
    return i

swaps = []

for _ in range(4):
    baseline = progress()
    for x in formulas:
        for y in formulas:
            if x == y: continue
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    swaps += [x, y]

print(",".join(sorted(swaps)))