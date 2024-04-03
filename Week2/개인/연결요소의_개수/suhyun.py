import sys
si = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = 0
for _ in range(m):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)

for x in range(1, n+1):
    if not visited[x]:
        dfs(x)
        ans += 1

print(ans)
