import math
def solution(k, d):
    answer = 0
    new_d = d/k
    for a in range(int(new_d)+1):
        b_max = min(a, int(math.sqrt(math.pow(new_d,2)-math.pow(a,2))))
        answer += (b_max+1)*2
        if b_max==a:
            answer -=1
        
    return answer 