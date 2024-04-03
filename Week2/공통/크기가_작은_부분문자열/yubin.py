def solution(t, p):
    answer = 0
    p_n = len(p)
    int_p = int(p)
    
    for start in range(len(t)-p_n+1):
        if int(t[start:start+p_n]) <= int_p:
            answer+=1
    return answer