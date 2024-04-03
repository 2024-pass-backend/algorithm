import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline
t = int(si())
dir = [[0,1], [1,0], [0,-1], [-1,0]]

def dfs(x, y):
    graph[x][y] = 0
    
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)
    

for i in range(t):
    m, n, k = map(int, si().split())
    graph = [[0] * m for _ in range(n)]
    for j in range(k):
        y, x = map(int, si().split())
        graph[x][y] = 1
    
    ans = 0
    for a, row in enumerate(graph):
        for b, col in enumerate(row):
            if graph[a][b] == 1:
                dfs(a, b)
                # print("a = " + str(a) + ", b = " + str(b))
                ans += 1
            # print(graph)
    print(ans)