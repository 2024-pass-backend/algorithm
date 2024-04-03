import sys
si = sys.stdin.readline

dir = [[0,1], [1,0], [0,-1], [-1,0]]

def dfs(x, y, graph, m, n):
    graph[x][y] = 0
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny, graph, m, n)
            
t = int(si())

for _ in range(t):
    answer = 0
    m, n, k = map(int, si().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, si().split())
        graph[x][y] = 1
    for i, row in enumerate(graph):
        for j, col in enumerate(row):
            if col == 1:
                dfs(i, j, graph, m, n)
                # print(graph)
                answer += 1
    print(answer)