with open("input.txt", "r") as f:
    inp = f.readlines()
    
inp = [x.strip().split(" ") for x in inp]
inp = [list(map(int, x)) for x in inp]

total = 0
is_increasing = False

for rep in inp:
    is_increasing =  rep[0] < rep[1]
    total += 1
    if is_increasing:
        for i in range(0, len(rep)-1):
            if (rep[i] >= rep[i+1]) or (1 < rep[i+1] - rep[i] > 3):
                total -= 1
                break
    elif not is_increasing:
        for i in range(0, len(rep)-1):
            if (rep[i] <= rep[i+1]) or (1 < rep[i] - rep[i+1] > 3):
                total -= 1
                break
    else:
        total -= 1

print(total)