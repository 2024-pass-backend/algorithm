def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    before = 0
    for target in targets:
        if before <= target[0]:
            before = target[1]
            answer += 1
    
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))