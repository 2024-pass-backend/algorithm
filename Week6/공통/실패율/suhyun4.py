# 3:35 ~ 
def solution(N, stages):
    answer = []
    
    a = len(stages)
    result = []
    for i in range(1, N+1):
        if a == 0:
            result.append([i, 0])
        else:
            val = stages.count(i) / a
            result.append([i, val])
            a -= stages.count(i)
    
    result.sort(key=lambda x:(-x[1], x[0]))
    # print(result)
    for n, val in result:
        answer.append(n)
    return answer

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))