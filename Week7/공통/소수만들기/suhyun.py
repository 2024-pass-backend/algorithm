from itertools import combinations
import math
def solution(nums):
    answer = 0
    
    for a in combinations(nums, 3):
        s = sum(a)
        if s < 2:
            continue
        is_sosu = False
        for i in range(2, int(math.sqrt(s)) + 1):
            if s % i == 0:
                is_sosu = True
                break
        
        if is_sosu == False:
            # print(a)
            answer += 1

    return answer

print(solution([1,2,3,4]))