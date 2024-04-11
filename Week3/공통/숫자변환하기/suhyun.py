# 8:56 ~ 9:03
# from collections import deque
from collections import deque
def solution(x, y, n):
    answer = 0
    
    if x == y:
        return 0
    else:
        queue = deque()
        visited = [0] * 1000001
        queue.append(x)
        while queue:
            xx = queue.popleft()
            if xx == y:
                break
            for i in range(3):
                if i == 0:
                    nx = xx + n
                elif i == 1:
                    nx = xx * 2
                else:
                    nx = xx * 3
                    
                if nx <= 0 or nx >= 1000001:
                    continue
                if visited[nx] == 0:
                    queue.append(nx)
                    visited[nx] = visited[xx] + 1
                
        return -1 if visited[y] == 0 else visited[y] 
    
print(solution(2, 5, 4))