# 4:10 ~ 
from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = len(queue1) * 3
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while sum1 != sum2:
        if sum1 > sum2:
            v = queue1.popleft()
            queue2.append(v)
            sum1 -= v
            sum2 += v
        elif sum1 < sum2:
            v = queue2.popleft()
            queue1.append(v)
            sum2 -= v
            sum1 += v
        answer += 1
        
        if answer == limit:
            return -1
        
    return answer

print(solution([3,2,7,2], [4,6,5,1]))