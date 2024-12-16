from collections import deque
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
costs = {(start_r, start_c, 0, 1): 0} # row, col, direction_row, direction_col : lowest_cost
target_cost = 999999999999999999
end_states = set()
paths = {}

while pr_queue:
    print(len(pr_queue))
    
    cost, r, c, dir_r, dir_c = heapq.heappop(pr_queue)
    
    if cost > costs.get((r, c, dir_r, dir_c)):
        continue

    if inp[r][c] == 'E':
        if cost > target_cost:
            break
        target_cost = cost
        end_states.add((r, c, dir_r, dir_c))

    for dr, dc in [(dir_r, dir_c), (-dir_c, dir_r), (dir_c, -dir_r)]:
        new_r = r + dr
        new_c = c + dc
        if dr == dir_r and dc == dir_c:
            new_cost = cost + 1  
        else:
            new_cost = cost + 1000

        if inp[new_r][new_c] == '#':
            continue
        
        # currently lowest cost, if location doesn't exist in dict give big number
        lowest = costs.get((new_r, new_c, dr, dc), 999999999999)
        
        if new_cost > lowest:
            break
        
        if new_cost < lowest:
            paths[(new_r, new_c, dr, dc)] = set()
            costs[(new_r, new_c, dr, dc)] = new_cost
        paths[(new_r, new_c, dr, dc)].add((r, c, dir_r, dir_c))
        heapq.heappush(pr_queue, (new_cost, new_r, new_c, dr, dc))

            
        bfs = deque(end_states)
        seen = set(end_states)
        
        while bfs:
            key = bfs.popleft()
            for last in paths.get(key, []):
                if last in seen:
                    continue
                seen.add(last)
                bfs.append(last)

print(len({(r, c) for r, c, _, _ in seen}))