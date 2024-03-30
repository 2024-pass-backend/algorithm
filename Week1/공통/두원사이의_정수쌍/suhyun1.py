# (큰 거에서 작은거를 뺸 후, + 1) * 4 ==> x축 y축위의 점들의 합
import math
def solution(r1, r2):
    answer = 0
    
    for r in range(1, r2):
        if r < r1:
            answer += (getMaxY(r2, r, "r2") - getMaxY(r1, r, "r1"))
        else:
            answer += getMaxY(r2, r, "r2") 
            
    answer *= 4
    answer += (r2 - r1 + 1) * 4 
    
    return answer

def getMaxY(rlen, r, rName):
    double_y = math.sqrt((rlen * rlen) - (r * r))
    int_y = int(double_y)
    if rName == "r1" and (double_y - int_y) == 0.0:
        return int_y - 1
    else:
        return int_y

print(solution(2, 3))
        