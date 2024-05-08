# 9:50 ~ 10:14
import sys
sys.setrecursionlimit(10000)
si = sys.stdin.readline
dir = [[0,1], [1,0], [0,-1], [-1,0]]
t = int(si())

def dfs(x, y):
    visited[x][y] = True
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
            continue
        
        if visited[nx][ny] == False and graph[nx][ny] == 1:
            dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, si().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, si().split())
        graph[y][x] = 1
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                cnt += 1
    print(cnt)