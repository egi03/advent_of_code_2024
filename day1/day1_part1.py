with open("input.txt", "r") as f:
    inp = f.read()

inp = inp.split("\n")
input_len = len(inp)
left = [0 for _ in range(input_len)]
right = [0 for _  in range(input_len)]


for i in range(input_len):
    left[i], right[i] = inp[i].split("   ")
    
    
left.sort()
right.sort()

total = 0

for i in range(input_len):
    total += abs(int(left[i]) - int(right[i]))
    
print(total)