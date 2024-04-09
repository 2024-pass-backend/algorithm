# 9:00 ~ 9:15
import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)
dir = [[0,1], [1,0], [0,-1], [-1,0]]
ans, no_land = 0, False

def dfs(x, y, visited, graph):
    global ans
    ans += int(graph[x][y])
    visited[x][y] = True
    for dx, dy in dir:
        xx = dx + x
        yy = dy + y
        if xx < 0 or yy < 0 or xx >= len(visited) or yy >= len(visited[0]):
            continue
        if not visited[xx][yy] and graph[xx][yy] != 'X':
            dfs(xx, yy, visited, graph)

def solution(maps):
    answer = []
    graph = [list(map) for map in maps]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    global ans, no_land
    for i, row in enumerate(graph):
        for j, col in enumerate(row):
            if col != 'X' and not visited[i][j]:
                dfs(i,j, visited, graph)
                answer.append(ans)
                no_land = True
                ans = 0
    
    if ans == 0 and not no_land:
        answer.append(-1)
    answer.sort()
    return answer

# maps = ["X591X","X1X5X","X231X", "1XXX1"]
maps = ["XXX","XXX","XXX"]	
print(solution(maps))
