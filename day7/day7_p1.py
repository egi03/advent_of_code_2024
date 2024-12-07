from itertools import product 

def calculate(equ, operats):
    eq = equ.copy()
    len_eq = len(eq)
    opers_id = 0
    total = 0

    while len(eq) > 1:
        eq[0] = eq[0] * eq[1] if operats[opers_id] == '*' else eq[0] + eq[1]
        opers_id += 1
        eq.pop(1)

    return eq[0]

def try_eval(equation):
    res, equ = equation.split(": ")
    res = int(res)
    num_of_operations = equ.count(" ")

    equ = equ.split(' ')
    equ = [int(x) for x in equ]

    # all permutations with repeating 
    possible_operations = [list(p) for p in product(['*','+'], repeat=num_of_operations)]

    for op in possible_operations:
        if calculate(equ, op) == res:
            return res
    return 0

with open("input.txt") as f:
    inp = f.read().splitlines()

print(sum([try_eval(eq) for eq in inp]))
