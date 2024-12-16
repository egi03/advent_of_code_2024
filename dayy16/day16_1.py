import heapq

with open('dayy16/input.txt') as f:
    inp = [list(x.strip()) for x in f.readlines()]


for r in range(len(inp)):
    for c in range(len(inp[0])):
        if inp[r][c] == 'S':
            start_r, start_c = r, c
        elif inp[r][c] == 'E':
            end_r, end_c = r, c
            
        
pr_queue = [(0, start_r, start_c, 0, 1)]
seen = set((start_r, start_c, 0, 1))


step = 0
while pr_queue:
    cost, r, c, dir_r, dir_c = heapq.heappop(pr_queue)
    seen.add((r, c, dir_r, dir_c))
    if inp[r][c] == 'E':
        print(cost)
        break

    
    for dr, dc in [(dir_r, dir_c), (-dir_c, dir_r), (dir_c, -dir_r)]:
        
        if dr == dir_r and dc == dir_c:
            new_r = r + dr
            new_c = c + dc
            new_cost = cost + 1
        else:
            new_r = r
            new_c = c
            new_cost = cost + 1000
        
        if inp[new_r][new_c] == '#':
            continue
        if (new_r, new_c, dr, dc) in seen:
            continue
        
        heapq.heappush(pr_queue, (new_cost, new_r, new_c, dr, dc))
            
