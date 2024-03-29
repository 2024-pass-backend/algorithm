import math
def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        max_y = math.floor(math.sqrt(r2**2 - x**2))
        min_y = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2 - x**2)))
        answer += max_y - min_y + 1
    return answer * 4
