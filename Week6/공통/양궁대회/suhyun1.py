from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    max_gap = -1
    
    for combi in combinations_with_replacement(range(11), n):
        info2 = [0] * 11
        
        for c in combi:
            info2[10-c] += 1
        
        a, l = 0, 0
        for i in range(11):
            if info[i] == info2[i] == 0:
                continue
            elif info[i] >= info2[i]:
                a += (10 - i)
            else:
                l += (10 - i)
        
        if l > a:
            gap = l - a
            if gap > max_gap:
                max_gap = gap
                answer = info2
                
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))