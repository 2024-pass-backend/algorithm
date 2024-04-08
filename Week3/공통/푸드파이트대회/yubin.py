# 10:31~
from collections import deque
def solution(food):
    answer = deque()
    answer.append("0")
    for i in range(len(food)-1, 0, -1):
        for _ in range(food[i]//2):
            answer.append(str(i))
            answer.appendleft(str(i))
            
    return ''.join(answer)