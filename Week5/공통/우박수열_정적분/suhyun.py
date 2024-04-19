# 문제가 이해가 안됨
def getList(k):
    arr = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
            arr.append(k)
        else:
            k = k * 3 + 1
            arr.append(k)
    return arr

def solution(k, ranges):
    arr_list = getList(k)
    answer = []
    
    for r in ranges:
        total = 0
        Range = arr_list[r[0] : len(arr_list)+r[1]] 
        # arr_list[0:6] > 0부터 5까지 > 5, 16, 8, 4
        # arr_list[0:5] > 0부터 4까지 > 5, 16, 8
        # arr_list[2:3] > 구간 2 > 실행안함
        # arr_list[3:3] > 구간 X, []
        
        
        # 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간
        if r[0] >= r[1] + len(arr_list):
            answer.append(-1)
            continue
        
        for i in range(len(Range)-1):
            total += ((Range[i] + Range[i+1] * 1) / 2)
        answer.append(total)
    return answer

ranges = [[0,0],[0,-1],[2,-3],[3,-3]]
print(solution(5, ranges))