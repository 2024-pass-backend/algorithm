from collections import deque
sx, sy, lx, ly, ex, ey = 0, 0, 0, 0, 0, 0
dir = [[0,1], [1,0], [0,-1], [-1,0]]

def bfs(startX, startY, endX, endY, maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque()
    queue.append([startX, startY, 0])
    visited[startX][startY] = True
    while queue:
        xx, yy, cnt = queue.popleft()
        
        if xx == endX and yy == endY:
            return cnt
        
        for d in dir:
            nx = xx + d[0]
            ny = yy + d[1]
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            
            if maps[nx][ny] == 'X':
                continue
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, cnt + 1])

    return 0
    
def solution(maps):
    
    for i, row in enumerate(maps):
        for j, col in enumerate(row):
            if col == 'S':
                sx, sy = i, j
            if col == 'L':
                lx, ly = i, j
            if col == 'E':
                ex, ey = i, j
                
    a = bfs(sx, sy, lx, ly, maps)
    b = bfs(lx, ly, ex, ey, maps)
            
    return -1 if a == 0 or b == 0 else a + b

print(solution(["SOEOL"]))