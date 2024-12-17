
def get_combo_operand(n):
    if 0 <= n <= 3:
        return n
    if n == 4:
        return A
    if n == 5:
        return B
    if n == 6:
        return C


with open("dayy17/input.txt") as f:
    inp = [x.strip() for x in f.readlines()]

A = int(inp[0][12:])
B = int(inp[1][12:])
C = int(inp[2][12:])

i_pointer = 0
instr = [int(x) for x in inp[4][9:] if x != ',']

results = []
while i_pointer < len(instr):
    opcode = instr[i_pointer]
    operand = instr[i_pointer + 1] if i_pointer + 1 < len(instr) else 0

    
    if opcode == 0:
        A //= 2 ** get_combo_operand(operand)
    elif opcode == 1:
        B = B ^ operand
    elif opcode == 2:
        B = get_combo_operand(operand) % 8
    elif opcode == 3:
        if A != 0:
            i_pointer = operand
            continue
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        results.append(str(get_combo_operand(operand) % 8))
    elif opcode == 6:
        B  = int(A / 2 ** get_combo_operand(operand))
    elif opcode == 7:
        C = int(A / 2 ** get_combo_operand(operand))
    i_pointer += 2

print(','.join(results))
