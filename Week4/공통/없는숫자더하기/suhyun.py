def solution(numbers):
    answer = 0
    
    for n in range(10):
        if n not in numbers:
            answer += n
    
    return answer

print(solution([1,2,3,4,6,7,8,0]))