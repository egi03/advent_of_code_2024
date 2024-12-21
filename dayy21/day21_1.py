from collections import deque
def get_shortest_sequences(keypad):
    coords = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] != '': 
                coords[keypad[r][c]] = (r, c)
                
    seqs = {}
    
    for x in coords:
        for y in coords:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            
            paths = []
            q = deque([(coords[x], "")])
            best_len = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, new_move in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]) or keypad[nr][nc] == '': 
                        continue

                    if keypad[nr][nc] == y:
                        if best_len < len(moves) + 1: 
                            break
                        best_len = len(moves) + 1
                        paths.append(moves + new_move + "A")
                    else:
                        q.append(((nr, nc), moves + new_move))
                else:
                    continue
                break
            seqs[(x, y)] = paths
    return seqs
    
from itertools import product
def get_shortest_path(keypad, code):
    code = 'A' + code
    seq = []
    for i in range(len(code)-1):
        x, y = code[i], code[i+1]
        seq.append(keypad[(x, y)])
        
    return [ "".join(x) for x in product(*seq) ]

        
        
def main():   
    with open("dayy21/input.txt") as f:
        inp = f.read().splitlines()
        
    num_pad = [['7','8','9'],
                ['4','5','6'],
                ['1','2','3'],
                ['', '0', 'A']]

    arrows = [['', '^', 'A'],
            ['<', 'v', '>']]

    num_seqs = get_shortest_sequences(num_pad)
    arrows_seqs = get_shortest_sequences(arrows)

    total = 0
    
    for code in inp:
        val1 = get_shortest_path(num_seqs,code)
        
        val2_candidates = []
        for v in val1:
            val2_candidates += get_shortest_path(arrows_seqs, v)
        best_len_2 = 999
        for v2 in val2_candidates:
            best_len_2 = min(len(v2), best_len_2)
        val2 = [x for x in val2_candidates if len(x) == best_len_2]
        
        
        val3_candidates = []
        for vv in val2:
            val3_candidates += get_shortest_path(arrows_seqs, vv)
        best_len_3 = 999
        for v3 in val3_candidates:
            best_len_3 = min(len(v3), best_len_3)
        val3 = [x for x in val3_candidates if len(x) == best_len_3]
        
        
        
        
        total += len(val3[0]) * int(code[:-1])
    
    print(total)
    
    
    
main()