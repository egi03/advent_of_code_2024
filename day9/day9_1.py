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

def move_file_blocks(inp):
    l = 0
    r = len(inp)-1
    
    while l < r:
        if inp[l] == '.':
            while inp[r] == '.':
                r -= 1
            inp[l], inp[r] = inp[r], inp[l]
        l += 1
    return inp

def calculate_checksum(inp):
    total = 0
    for i,n in enumerate(inp):
        if n == '.':
            break
        total += i * int(n)
        
    return total

def main():
    with open("day9/input.txt") as f:
        inp = f.read()
        
        
    print(calculate_checksum(move_file_blocks(generate_map(inp))))



if __name__ == "__main__":
    main()