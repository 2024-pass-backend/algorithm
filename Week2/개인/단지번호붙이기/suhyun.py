import sys
si = sys.stdin.readline
n = int(si())
graph = []
ans = 0
dir = [[0,1], [1,0], [0,-1], [-1,0]]
for _ in range(n):
    graph.append(list(si().strip()))
    
# print(type(map(int, input().split(' '))))
    
def dfs(x, y):
    global answer
    answer += 1
    graph[x][y] = '0'
    
    for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if graph[nx][ny] == '1':
                dfs(nx, ny)
        
    return answer
        
house = []
answer = 0
for i, row in enumerate(graph):
    for j, col in enumerate(row):
        if col == '1':
        # if graph[i][j] == '1':
            # print("탔음")
            cnt = dfs(i,j)
            answer = 0
            ans += 1
            house.append(cnt)

house.sort()
print(ans)
for i in house:
    print(i)

          
