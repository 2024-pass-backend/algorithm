# from collections import deque
# queue = deque([start])
# while queue:
# v = queue.popleft()
import sys
from collections import deque
si = sys.stdin.readline

def dfs(graph, x, visited):
    visited[x] = True
    print(x, end=' ')
    for y in graph[x]:
        if not visited[y]:
            dfs(graph, y, visited)

def bfs(graph, x, visited):
    visited[x] = True
    queue = deque([x])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for y in graph[v]:
            if not visited[y]:
                queue.append(y)
                visited[y] = True 
        
        

n, m, v = map(int, si().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1) 
for _ in range(m):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(graph, v, visited)
visited = [False] * (n + 1)
print()
bfs(graph, v, visited)

    