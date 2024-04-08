# 10:00 ~ 10:13
def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            answer += str(i)
    
    answer += str(0)
    a = answer[::-1]
    answer += a[1:]
    
    return answer

food = [1, 7, 1, 2]
print(solution(food))