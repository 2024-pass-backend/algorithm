from itertools import cycle
def solution(n):
    wm = cycle('수박')
    answer = []
    for _, i in zip(range(n), wm):
        answer.append(i)
    return ''.join(answer)