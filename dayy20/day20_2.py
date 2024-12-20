from collections import deque

with open("dayy20/input.txt") as f:
    grid = [ x.strip() for x in f.readlines() ]

rows = len(grid)
cols = len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            sr, sc = r, c
            break
    else:
        continue
    break

distances = [ [-1] * cols for _ in range(rows) ]
distances[sr][sc] = 0
queue = deque([(sr, sc)])


while queue:
    r, c = queue.popleft()
    
    for nr, nc in [(r-1, c), (r+1,c), (r,c-1), (r,c+1)]:
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == '#':
            continue
        
        # check if node is already visited
        if distances[nr][nc] != -1:
            continue
        
        distances[nr][nc] = distances[r][c] + 1
        queue.append((nr, nc))
        if grid[nr][nc] == 'E':
            end_distance = distances[nr][nc]
            
total = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '#':
            continue
        
        for dis in range(2, 21):
            for temp_r in range(dis+1):
                temp_c = dis - temp_r

                for nr, nc in {(r+temp_r,c + temp_c), (r+temp_r,c-temp_c), (r-temp_r, c+temp_c), (r-temp_r, c-temp_c)}:
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == '#':
                        continue
        
                    if distances[r][c] - distances[nr][nc] >= 100 + dis:
                        total += 1
                
                
print(total)
            
        