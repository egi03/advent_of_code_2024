
locks = []
keys = []
with open("dayy25/input.txt") as f:
    for block in f.read().split("\n\n"):
        temp = []
        for s in block.splitlines():
            temp.append([c for c in s])
        
        final_val = []
        
        for c in range(5):
            val = 0
            for r in range(7):
                if temp[r][c] == '#':
                    val += 1
            final_val.append(val-1)
            
        if temp[0][0] == "#":
            locks.append(final_val)
                
        else:
            keys.append(final_val)


total = 0

for lock in locks:
    for key in keys:
        if all(x + y <= 5 for x, y in zip(lock, key)):
            total += 1

print(total)