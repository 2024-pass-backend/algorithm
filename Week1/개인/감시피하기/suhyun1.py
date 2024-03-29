# 이거까지만 풀고 잡아바 어플라이 자격증 감면 신청
import sys

def pro(x):
    if x == 3:
        if(bfs()):
            print("YES")
            sys.exit(0)
    
    else:
        for i, row in enumerate(graph):
            for j, col in enumerate(row):
                if graph[i][j] == "X":
                    graph[i][j] = "O"
                    pro(x + 1)
                    graph[i][j] = "X"

def bfs():
    dir = [[-1,0], [1,0], [0,-1], [0,1]]
    for teacher in teachers:
        x, y = teacher
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            while(isIn(nx, ny)):
                if graph[nx][ny] == "O":
                    break
                
                if graph[nx][ny] == "S":
                    return False
                
                
                nx += dir[i][0]
                ny += dir[i][1]
        
    return True


def isIn(x, y):
    return (0 <= x < n) and (0 <= y < n)
        

si = sys.stdin.readline
n = int(si())
teachers = []
graph = []

for i in range(n):
    graph.append(list((map(str, si().split()))))
    for j in range(n):
        if graph[i][j] == "T":
            teachers.append((i, j))

pro(0)
print("NO")
     