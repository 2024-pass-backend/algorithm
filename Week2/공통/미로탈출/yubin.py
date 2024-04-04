from collections import deque
def solution(maps):
    answer = 0
    h, w = len(maps), len(maps[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 범위 이탈
    def OoR(x, y):
        return (x<0) or (y<0) or (x>=w) or (y>=h)
    
    def bfs(x, y, end):
        que = deque([(x, y)])
        visited = [[-1] * w for _ in range(h)]
        visited[y][x] += 1
        
        while que:
            sx, sy = que.popleft()
            for dx, dy in direction:
                nx = sx+dx
                ny = sy+dy
                if OoR(nx, ny) or visited[ny][nx]!=-1:
                    continue
                if maps[ny][nx] == end:
                    return visited[sy][sx] + 1
                if maps[ny][nx] != 'X':
                    que.append((nx, ny))
                    visited[ny][nx] = visited[sy][sx] + 1
        return -1
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                start_x, start_y = j, i
            elif maps[i][j] == 'E':
                exit_x, exit_y = j, i
            elif maps[i][j] == 'L':
                lever_x, lever_y = j, i
    
    visited1 = bfs(start_x, start_y, 'L')
    if visited1 == -1:
        return -1
    
    visited2 = bfs(lever_x, lever_y, 'E')
    if visited2 == -1:
        return -1
    
    return visited1+visited2