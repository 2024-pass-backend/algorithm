def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x : x[1])
    before = 0
    
    for t in targets:
        if before <= t[0]:
            before = t[1]
            answer += 1
    
    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))