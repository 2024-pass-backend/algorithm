def rotate_array(arr, sx, sy, ex, ey):
    tmp = arr[sx][sy]
    min_val = tmp
    for i in range(sx, ex):
        min_val = min(min_val, arr[i][sy])
        if i + 1 < ex:
            arr[i][sy] = arr[i + 1][sy]
    for i in range(sy, ey):
        min_val = min(min_val, arr[ex - 1][i])
        if i + 1 < ey:
            arr[ex - 1][i] = arr[ex - 1][i + 1]
    for i in range(ex - 1, sx - 1, -1):
        min_val = min(min_val, arr[i][ey - 1])
        if i - 1 >= sx:
            arr[i][ey - 1] = arr[i - 1][ey - 1]
    for i in range(ey - 1, sy - 1, -1):
        min_val = min(min_val, arr[sx][i])
        if i - 1 >= sy:
            arr[sx][i] = arr[sx][i - 1]
    arr[sx][sy + 1] = tmp
    return min_val

def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = n
            n += 1
    for q in queries:
        sx, sy, ex, ey = q
        answer.append(rotate_array(arr, sx - 1, sy - 1, ex, ey))
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))