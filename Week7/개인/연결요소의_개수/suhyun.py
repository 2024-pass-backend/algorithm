import sys
si = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, si().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def dfs(v):
    visited[v] = True
    for n in graph[v]:
        if visited[n] == False:
            dfs(n)
cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt) 
    