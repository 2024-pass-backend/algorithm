from collections import deque
def solution(arr):
    que = deque(arr)
    answer = []
    while que:
        x = que.popleft()
        if len(que)==0 or x!=que[0]:
            answer.append(x)
    return answer