def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    # print(data)
    for i in range(row_begin-1, row_end):
        sum = 0
        for j in data[i]:
            sum += (j % (i+1))
        # print("합")
        # print(sum)    
        answer = answer ^ sum
    
    return answer

data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
print(solution(data, 2, 2, 3))