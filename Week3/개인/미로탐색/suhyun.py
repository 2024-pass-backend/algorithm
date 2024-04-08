import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
dir = [[0,1], [1,0], [0,-1], [-1,0]]
graph = [list(map(int, si().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    visited[x][y] = True
    queue = deque()
    queue.append([x, y])
    while queue:
        xx, yy = queue.popleft()
        for dx, dy in dir:
            nx = xx + dx
            ny = yy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append([nx, ny])
            graph[nx][ny] = graph[xx][yy] + 1
            
bfs(0, 0)
print(graph[n-1][m-1])

        