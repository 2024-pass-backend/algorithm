def solution(k, tangerine):
    answer = 0
    
    a = [0] * 10000001
    # 1 - 1개
    # 2 - 2개
    # 3 - 2개
    # 4 - 1개
    # 5 - 2개
    
    for t in tangerine:
        a[t] += 1
        
    a.sort(reverse=True)
    c = 0
    
    for aa in a:
        if aa == 0:
            break
        if c < k:
            c += aa
        else:
            break
        answer += 1
        
    return answer

tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(6, tangerine))