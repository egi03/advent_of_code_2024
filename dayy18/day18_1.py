from collections import deque


with open("dayy18/input.txt") as f:
    inp = [list(map(int, x.split(','))) for x in f.read().splitlines()]
    

grid_len = 70
grid = [[0] * (grid_len + 1) for _ in range(grid_len + 1)]

for c, r in inp[:1024]:
    grid[r][c] = 1


directions = [(0,1), (0,-1), (1,0), (-1,0)]
queue = deque([(0, 0, 0)]) # x, y, cost
visited = set((0, 0))

while queue:
    x, y, distance = queue.popleft()
    
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx <= grid_len and 0 <= ny <= grid_len and (nx, ny) not in visited and grid[nx][ny] == 0:
            if nx == ny == 70:
                print(distance + 1)
            visited.add((nx, ny))
            queue.append((nx, ny, distance + 1))
    