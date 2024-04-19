# https://haesoo9410.tistory.com/193
# 2차원 배열 정렬시
# 배열.sort(key=lambda x: (x[0], -x[1]))
# 위와 같이 작성하면 2차원배열에 대해 0번째컬럼을 기준으로 오름차순, 같다면 1번째 컬럼을 기준으로 내림차순

def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x: (x[col-1], -x[0]))
    print(data)
    
    for i in range(row_begin-1, row_end):
        sum = 0
        for k in range(len(data[0])):
            sum += (data[i][k] % (i+1))
        # print(sum)
        answer = answer ^ (sum)    
    
    return answer

data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
print(solution(data, 2, 2, 3))