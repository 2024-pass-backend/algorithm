import math
def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        min_y = math.ceil(math.sqrt(max(0, r1**2 - x**2)))
        max_y = int(math.sqrt(r2**2 - x**2))
        
        answer += max_y-min_y+1
        
        # print(answer)
    return answer*4