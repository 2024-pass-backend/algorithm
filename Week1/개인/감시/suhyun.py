import sys, copy
si = sys.stdin.readline
n, m = map(int, si().split())
remain, cnt, ans = n*m, 0, sys.maxsize 
graph = []
cctvs = []
dir = [[0,1],[1,0],[0,-1],[-1,0]] # 동 남 서 북
cctv = [
    [[0]],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,3],[0,1],[1,2],[2,3]],
    [[0,2,3],[0,1,3],[1,2,3],[0,1,2]],
    [[0,1,2,3]]
]

for i in range(n):
    graph.append(list(map(int, si().split())))
    for j in range(m):
        if graph[i][j] >= 1 and graph[i][j] <= 5:
            cctvs.append([graph[i][j], i, j])
        if graph[i][j] != 0:
            remain -= 1
    cnt = len(cctvs)

def observation(d, graph, x, y):
    global n, m
    count = 0
    
    for direction in d:
        nx, ny = x, y
        while True:
            nx += dir[direction][0]
            ny += dir[direction][1]
            
            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                break
            
            if graph[nx][ny] == 6:
                break
            
            if graph[nx][ny] == -1 or (graph[nx][ny] >= 1 and graph[x][ny] <= 5):
                continue
            
            graph[nx][ny] = -1
            count += 1
    
    return count

def pro(idx, graph, remain):
    global cnt, ans
    if idx == cnt:
        ans = min(remain, ans)
        return
    
    else:
        new_graph = copy.deepcopy(graph)
        type, x, y = cctvs[idx]
        for d in cctv[type]:
            count = 0
            count += observation(d, new_graph, x, y)
            pro(idx + 1, new_graph, remain - count)
            new_graph = copy.deepcopy(graph)


pro(0, graph, remain)
print(ans)
            