def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])
    
    mx = -0.5
    
    for s, e in targets:
        if s > mx:
            mx = e - 0.5
            answer += 1
            
    return answer