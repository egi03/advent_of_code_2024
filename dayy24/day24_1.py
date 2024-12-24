with open("dayy24/input.txt") as f:
    values = {}
    formulas = {}

    for line in f:
        if line.isspace(): break
        x, y = line.split(": ")
        values[x] = int(y)

    for line in f:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)

is_done = False

new_formulas = formulas.copy()

while new_formulas:
    for k, f in formulas.items():
        all_values = values.keys()
        op, x, y = f
        if x in all_values and y in all_values:
            new_formulas.pop(k)
            if op == "AND":
                values[k] = values[x] & values[y]
            elif op == "OR":
                values[k] = values[x] | values[y]
            elif op == "XOR":
                values[k] = values[x] ^ values[y]
    formulas = new_formulas.copy()


values = dict(sorted(values.items(), reverse=True))
all_z = [str(v) for k, v in values.items() if k[0] == 'z']

print("Bin:", bin_z := "".join(all_z))
print(int(bin_z, 2))