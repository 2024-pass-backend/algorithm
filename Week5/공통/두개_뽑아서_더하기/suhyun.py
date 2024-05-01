def solution(numbers):
    answer = set()
    numbers.sort()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    
    a = sorted(list(answer))
    return a

print(solution([2,1,3,4,1]))