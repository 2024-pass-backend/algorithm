answer = [0,0]
def getPrint(a):
    for row in a:
        print(*row)
    print('------------')


def getCount(arr):
    if arr[0][0] == 0:
        answer[0] += 1
    else:
        answer[1] += 1

def check(arr):
    sa = arr[0][0]
    for row in arr:
        for col in row:
            if col != sa:
                return False
    return True

def partition(arr):
    if len(arr) == 1:
        getCount(arr)
        # print(answer)
        return
    
    #모든 수가 같거나
    if check(arr):
        if arr[0][0] == 1:
            answer[1] += 1
        else:
            answer[0] += 1
        return
    
    # getPrint(arr)
    a = [[0] * (len(arr[0]) // 2) for _ in range(len(arr) // 2)]
    # 1사분면
    r, c = 0, 0
    for row in range(0, len(arr)// 2):
        for col in range(0, len(arr[0]) // 2):
            a[r][c] = arr[row][col]
            c += 1
        c = 0
        r += 1
    partition(a)
    # 2사분면
    r, c = 0, 0
    for row in range(0, len(arr) // 2):
        for col in range(len(arr[0]) // 2, len(arr[0])):
            a[r][c] = arr[row][col]
            c += 1
        c = 0
        r += 1
    partition(a)
    # 3사분면
    r, c = 0, 0
    for row in range(len(arr) // 2, len(arr)):
        for col in range(0, len(arr[0]) // 2):
            a[r][c] = arr[row][col]
            c += 1
        c = 0
        r += 1
    partition(a)
    # 4사분면
    r, c = 0, 0
    for row in range(len(arr) // 2, len(arr)):
        for col in range(len(arr[0]) // 2, len(arr[0])):
            a[r][c] = arr[row][col]
            c += 1
        c = 0
        r += 1
    partition(a)
    

def solution(arr):
    
    partition(arr)
    
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))