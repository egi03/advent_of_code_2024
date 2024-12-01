with open("input.txt", "r") as f:
    inp = f.read()

inp = inp.split("\n")
input_len = len(inp)
left = [0 for _ in range(input_len)]
right = [0 for _  in range(input_len)]


for i in range(input_len):
    left[i], right[i] = inp[i].split("   ")

total = sum([int(num) * right.count(num) for num in left])

print(total)