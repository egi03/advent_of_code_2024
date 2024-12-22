def get_next_secret_num(num):
    num = (num * 64) ^ num
    num %= 16777216
    num = (num // 32) ^ num
    num %= 16777216
    num = (num * 2048) ^ num
    num %= 16777216
    return num

# (s1,s2,s3,s4): bananas
seqs = {}

for n in open("dayy22/input.txt").read().splitlines():
    prices = []
    changes = []    
    prev_price = int(n) % 10
    for _ in range(2000):
        n = get_next_secret_num(int(n))
        price = int(n) % 10
        prices.append(int(price))
        changes.append(int(price) - int(prev_price))
        prev_price = price
    
    temp_seqs = {}
    for i in range(len(changes)-3):
        seq = tuple(changes[i:i+4])
        if seq in temp_seqs:
            continue
        else:
            temp_seqs[seq] = prices[i+3]

    for s in temp_seqs.keys():
        if s in seqs:
            seqs[s] += temp_seqs[s]
        else:
            seqs[s] = temp_seqs[s]
            
            
max_seq = max(seqs, key=seqs.get)
max_value = seqs[max_seq]
print(f"Max seq: {max_seq}")
print("Result: ", max_value)