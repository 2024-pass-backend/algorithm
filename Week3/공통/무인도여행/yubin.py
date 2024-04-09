from collections import deque
def solution(maps):
    # global maps
    answer = []
    h, w = len(maps), len(maps[0])
    
    fourway = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def OoR(x, y):
        return (x<0) or (y<0) or (x>=w) or (y>=h)
    
    global visited
    visited = [[False]*w for _ in range(h)]
    def bfs(x, y):
        que = deque([(x, y)])
        food = int(maps[y][x])
        visited[y][x] = True
        
        while que:
            nx, ny = que.popleft()
            for dx, dy in fourway:
                sx = nx+dx
                sy = ny+dy
                # 범위 이탈 or 이미 방문 or 바다
                if OoR(sx, sy) or visited[sy][sx] or (maps[sy][sx]=='X'):
                    continue
                # 식량 있는 경우
                que.append((sx, sy))
                food += int(maps[sy][sx])
                visited[sy][sx] = True

        return food
    
    for i in range(h):
        for j in range(w):
            if (maps[i][j] != 'X') & (visited[i][j] != True):
                f = bfs(j, i)
                answer.append(f)
                
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)