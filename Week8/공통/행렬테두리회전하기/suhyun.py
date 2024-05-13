# 9:40 ~ 10:06 달팽이 숫자 먼저 해보기
# 10:48 ~  
# 틀린 코드(시간초과코드)
import copy
def solution(rows, columns, queries):
    answer = []
    n = 1
    arr1 = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for col in range(columns):
            arr1[row][col] = n
            n += 1
    
    for q in queries:
        sx, sy, ex, ey = q
        # arr2 = copy.deepcopy(arr1)
        min_val = 101
        # 왼쪽세로
        for s in range(sx-1, ex-1):
            min_val = min(arr1[s+1][sy-1], min_val)
            arr1[s][sy-1] = arr1[s+1][sy-1]
        # 하단
        for s in range(sy-1, ey-1):
            min_val = min(arr1[ex-1][s+1], min_val)
            arr1[ex-1][s] = arr1[ex-1][s+1]
        # 오른쪽세로
        for s in range(sx-1, ex-1):
            min_val = min(arr1[s][ey-1], min_val)
            arr1[s+1][ey-1] = arr1[s][ey-1]
        # 상단
        for s in range(sy-1, ey-1):
            min_val = min(arr1[sx-1][s], min_val)
            arr1[sx-1][s+1] = arr1[sx-1][s]
        answer.append(min_val)
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))