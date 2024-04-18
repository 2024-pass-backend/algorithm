# import copy
# 새로운 배열 = copy.deepcopy(배열)
# 기존 배열을 변경하더라도 새로운 배열에 영향을 미치지 않는다.
import sys, copy
si = sys.stdin.readline

dir = [[0,1], [1,0], [0,-1], [-1,0]] # 동, 남, 서, 북 방향
cctv = [
    [[0]],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,3],[0,1],[1,2],[2,3]],
    [[0,2,3],[0,1,3],[0,1,2],[1,2,3]],
    [[0,1,2,3]]    
]
cctvs = []

n, m = map(int, si().split())
arr = []
ans = n * m

for i in range(n):
    arr.append(list(map(int, si().split())))
    for j in range(m):
        if arr[i][j] != 0:
            ans -= 1
        if arr[i][j] >= 1 and arr[i][j] <= 5:
            cctvs.append([i, j, arr[i][j]])

def monitor(new_map, x, y, direction):
    cnt = 0
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dir[d][0]
            ny += dir[d][1]
            if isIn(nx, ny) == False:
                break 
            
            if new_map[nx][ny] == 6:
                break
            
            if new_map[nx][ny] == 0:
                cnt += 1
                new_map[nx][ny] = -1
            
    return cnt

def isIn(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

def pro(idx, arr, remain):
    global ans
    if idx == len(cctvs):
        ans = min(remain, ans)
        return
    else:
        new_map = copy.deepcopy(arr)

        # 만약 꺼낸 cctv가 2번이라면 [0,2] / [1,3] 진행시켜야함
        x, y, cc = cctvs[idx]
        for i in range(len(cctv[cc])):
            cnt = 0
            cnt += monitor(new_map, x, y, cctv[cc][i])
            pro(idx + 1, new_map, remain - cnt)
            new_map = copy.deepcopy(arr)

pro(0, arr, ans)
print(ans)