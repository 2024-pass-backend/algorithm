import sys
si = sys.stdin.readline
c = int(si())
n = int(si())
graph = [[] for _ in range(c+1)] # 항상 헷갈려. 파이썬에서는 그래프 초기화를 [[] for _ in range(n)] 으로 하나?
visited = [False] * (c+1)
cnt = 0

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = True
    for a in graph[v]:
        if not visited[a]:
            dfs(a)
        

for i in range(n):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

dfs(1)
# print(visited)
print(cnt-1)