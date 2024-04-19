# sys.exit(0) > 종료
import sys
si = sys.stdin.readline
n = int(si())
arr = []
blank = []
teachers = []
dir = [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(n):
    arr.append(list(si().split()))
    for j in range(n):
        if arr[i][j] == 'X':
            blank.append([i,j])
        if arr[i][j] == 'T':
            teachers.append([i,j])

def isIn(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def monitor():
    for t in teachers:
        tx, ty = t #선생님의 위치
        for d in dir:
            nx, ny = tx, ty
            while True:
                nx += d[0]
                ny += d[1]
                
                if not isIn(nx, ny):
                    break
                
                if arr[nx][ny] == 'S':
                    return False
                
                if arr[nx][ny] == 'O':
                    break
    return True

def pro(idx, cnt):
    if cnt == 3:
        if monitor():
            print("YES")
            sys.exit(0)
        return
    if idx >= len(blank):
        return
    else:
        arr[blank[idx][0]][blank[idx][1]] = 'O'
        pro(idx + 1, cnt + 1)
        arr[blank[idx][0]][blank[idx][1]] = 'X'
        pro(idx + 1, cnt)
        

pro(0, 0)
print("NO")