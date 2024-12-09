def generate_map(inp):
    new_map = []
    index = 0
    for i,n in enumerate(inp):
        if i % 2 == 0:
            for _ in range(int(n)):
                new_map.append(index)
            index += 1
        else:
            for _ in range(int(n)):
                new_map.append('.')
            
    return new_map

def get_empty_locations(inp):
    empty_locations = []
    i = 0
    while i < len(inp):
        if inp[i] == '.':
            j = i
            while inp[j] == '.':
                j += 1
            empty_locations.append([i, j])
            i = j
        else:
            i += 1
    return empty_locations

def move_blocks(inp):
    empty_locations = get_empty_locations(inp)
    
    i = len(inp) - 1 
    while i > 0:
        if inp[i] == '.':
            i -= 1
            continue
        
        block_num = inp[i]
        r = i + 1
        l = i + 1
        while inp[l-1] == block_num:
            l -= 1
        block_size = r-l
        for e in empty_locations:
            empty_size = e[1] - e[0]
            if block_size > empty_size:
                continue
            if e[0] < l:
                inp[e[0]: e[0] + block_size], inp[l: r] = inp[l: r], inp[e[0]: e[0] + block_size]
                e[0] += block_size
                break
        i = l-1
    return inp

def calculate_checksum(inp):
    total = 0
    for i,n in enumerate(inp):
        if n == '.':
            continue
        total += i * int(n)
        
    return total




def main():
    with open("day9/input.txt") as f:
        inp = f.read()
        
    print(calculate_checksum(move_blocks(generate_map(inp))))



if __name__ == "__main__":
    main()