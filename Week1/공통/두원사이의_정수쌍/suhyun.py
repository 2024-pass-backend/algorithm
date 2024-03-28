## int(y)
## rName == "r1"
## && -> and

import math
def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2):
        if x < r1:
            answer += (getMaxY(x, r2, "r2") - getMaxY(x, r1, "r1"))
        else:
            answer += (getMaxY(x, r2, "r2"))

    answer *= 4
    answer += (r2 - r1 + 1) * 4
    
    return answer

def getMaxY(x, r, rName):
    y = math.sqrt(r * r - x * x)
    maxY = int(y)
    if rName == "r1" and y - maxY == 0.0:
        return maxY - 1
    return maxY

print(solution(2, 3))