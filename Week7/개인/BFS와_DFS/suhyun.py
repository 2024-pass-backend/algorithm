# 9:28 ~ 9:50
from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for n in graph[v]:
        if visited[n] == False:
            dfs(n)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        n = q.popleft()
        print(n, end=' ')
        for s in graph[n]:
            if visited[s] == False:
                visited[s] = True
                q.append(s)
        

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)