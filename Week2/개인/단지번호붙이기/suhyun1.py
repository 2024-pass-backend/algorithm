import sys
si = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(si())
graph = [list(map(int, si().strip())) for _ in range(n)]
dir = [[0,1], [1,0], [0,-1], [-1,0]]
answer = []
ans = 0

def dfs(x, y):
    global ans
    ans += 1
    graph[x][y] = 0
    
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)
    

for x, row in enumerate(graph):
    for y, col in enumerate(row):
        if col == 1:
            dfs(x, y)
            answer.append(ans)
            ans = 0

print(len(answer))
answer.sort()
for i in answer:
    print(i)