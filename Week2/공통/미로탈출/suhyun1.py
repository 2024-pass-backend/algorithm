# queue = deque()
# while queue:
# nx, ny, cnt = queue.popleft()
from collections import deque

sx, sy, lx, ly, ex, ey = 0, 0, 0, 0, 0, 0
dir = [[0,1], [1, 0], [0, -1], [-1, 0]]

def bfs(maps, startX, startY, tX, tY):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque()
    queue.append([startX, startY, 0])
    visited[startX][startY] = True
    while queue:
        x, y, cnt = queue.popleft()
        if x == tX and y == tY:
            return cnt
        
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            
            if maps[nx][ny] == 'X':
                continue
            
            if not visited[nx][ny]:
                queue.append([nx, ny, cnt + 1])
                visited[nx][ny] = True
    return 0       

def solution(maps):
    
    for i, row in enumerate(maps):
        for j, col in enumerate(row):
            if col == 'S':
                sx, sy = i, j
            elif col == 'E':
                ex, ey = i, j
            elif col == 'L':
                lx, ly = i, j
    
    before = bfs(maps, sx, sy, lx, ly)
    after = bfs(maps, lx, ly, ex, ey)
    if before == 0 or after == 0:
        return -1
            
    return before + after

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))