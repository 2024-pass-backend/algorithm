# 2:45 ~ 
def solution(n, m, section):
    answer = 0
    
    start = 0
    for s in section:
        if start < s:
            start = s + m - 1
            answer += 1

    return answer

# print(solution(8, 4, [2, 3, 6]))
print(solution(4, 1, [1,2,3,4]))