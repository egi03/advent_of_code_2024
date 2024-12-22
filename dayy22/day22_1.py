def get_next_secret_num(num):
    num = (num * 64) ^ num
    num %= 16777216
    num = (num // 32) ^ num
    num %= 16777216
    num = (num * 2048) ^ num
    num %= 16777216
    return num

total = 0
for n in open("dayy22/input.txt").read().splitlines():
    for _ in range(2000):
        n = get_next_secret_num(int(n))
    total += int(n)
    
print(total)