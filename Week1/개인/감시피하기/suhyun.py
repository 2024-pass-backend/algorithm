# 자바에서 List<Node> list = new ArrayList<Node>(); list.add(new Node(i,j));
# 파이썬에서는 단순히 teacher = [] teacher.add([i,j])

# map초기화시, graph = [], graph.append(리스트)로 하면 2차원 배열 초기화됨.
import sys

def pro(cnt):
    global flag
    
    if cnt == 3:
        if bfs():
            flag = True
            # return
            print("YES")
            sys.exit(0)
    
    else:
        for x in range(n):
            for y in range(n):
                if graph[x][y] == "X":
                    graph[x][y] = "O"
                    pro(cnt + 1)
                    graph[x][y] = "X"

def bfs():
    # 동, 서, 남, 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for t in teacher: # t는 선생님의 위치 ex) (0,1)
        for k in range(4):
            nx, ny = t
            
            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == "O":
                    break
                
                if graph[nx][ny] == "S":
                    return False
                
                nx += dx[k]
                ny += dy[k]
    return True
    
    

si = sys.stdin.readline
n = int(si())
flag = False
graph = []
teacher = []

for i in range(n):
    graph.append(list(map(str, si().split())))
    for j in range(n):
        if graph[i][j] == "T":
            teacher.append([i, j])

pro(0)

print("YES" if flag else "NO")
# if flag:
#     print("YES")
# else:
#     print("NO")