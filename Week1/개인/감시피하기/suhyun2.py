import sys

dir = [[-1,0],[1,0],[0,-1],[0,1]]

def pro(idx, cnt):
    if cnt == 3:
        if(bfs()):
            print("YES")
            sys.exit(0)
        return
    
    if idx > b:
        return
    
    else:
        graph[blank[idx][0]][blank[idx][1]] = "O"
        pro(idx + 1, cnt + 1)
        graph[blank[idx][0]][blank[idx][1]] = "X"
        pro(idx + 1, cnt)
        
def bfs():
    global dir
    for t in teachers:
        x, y = t
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
n, b = int(si()), 0
graph = []
teachers = []
blank = [[0, 0] for _ in range(n * n + 1)] ## 2차원 배열로 초기화해야함.

for i in range(n):
    graph.append(list(map(str, si().split())))
    for j in range(n):
        if graph[i][j] == "T":
            teachers.append((i, j))
        elif graph[i][j] == "X":
            b += 1
            blank[b][0] = i
            blank[b][1] = j

pro(1, 0)
print("NO")
 
