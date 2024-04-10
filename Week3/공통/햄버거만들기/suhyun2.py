def solution(ingredient):
    answer = 0
    
    stack = []
    for elem in ingredient:
        stack.append(elem)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
    
    return answer

print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))