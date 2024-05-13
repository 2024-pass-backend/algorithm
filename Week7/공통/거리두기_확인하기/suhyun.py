from itertools import combinations
from collections import deque
import math
dir = [[0,1], [1,0], [0,-1], [-1,0]]
def solution(places):
    answer = []
    for place in places:
        people = []
        for i, row in enumerate(place):
            for j, col in enumerate(row):
                if col == 'P':
                    people.append([i,j])
        
        c = False
        for per in combinations(people, 2):
            if bfs(per[0][0], per[0][1], per[1][0], per[1][1], place) <= 2:
                answer.append(0)
                c = True
                break
        
        if c == False:
            answer.append(1)
    return answer

def getPrint(graph, sx, sy, ex, ey):
    print(sx, sy, ex, ey)
    for row in graph:
        print(*row)
    print("=======")

def bfs(sx, sy, ex, ey, place):
    graph = [[0] * len(place[0]) for _ in range(len(place))]
    q = deque([(sx, sy)])
    graph[sx][sy] = 0
    while q:
        n = q.popleft()
        xx, yy = n
        if xx == ex and yy == ey:
            break
        
        for dx, dy in dir:
            nx = xx + dx
            ny = yy + dy
            if nx < 0 or ny < 0 or nx >= len(place) or ny >= len(place[0]):
                continue
                
            if place[nx][ny] == 'X':
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[xx][yy] + 1
                q.append((nx, ny))

    getPrint(graph, sx, sy, ex, ey)
    return 3 if graph[ex][ey] == 0 else graph[ex][ey] 

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]))