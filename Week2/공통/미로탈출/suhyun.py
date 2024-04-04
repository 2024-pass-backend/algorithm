from collections import deque
sx, sy, lx, ly, ex, ey = 0, 0, 0, 0, 0, 0
dir = [[0,1], [1,0], [0,-1], [-1,0]]

def bfs(startX, startY, targetX, targetY, maps):
    
    visited = [[False] * (len(maps[0])) for _ in range(len(maps))]
    queue = deque()
    queue.append([startX, startY, 0])
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == targetX and y == targetY:
            return cnt
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 'X' or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append([nx, ny, cnt + 1])
    return -1
    
def solution(maps):
    answer = 0
    global sx, sy, lx, ly, ex, ey
    for i, row in enumerate(maps):
        for j, col in enumerate(row):
            if col == 'S':
                sx, sy = i,j
            elif col == 'L':
                lx, ly = i,j
            elif col == 'E':
                ex, ey = i,j
    
    before = bfs(sx, sy, lx, ly, maps)
    after = bfs(lx, ly, ex, ey, maps)
    if before == -1 or after == -1:
        answer = -1
    else:
        answer = before + after
    return answer

maps = ["SOEOL"]
print(solution(maps))