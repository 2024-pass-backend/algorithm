import math
def solution(n):
    answer = 0
    a = int(math.sqrt(n))
    if a * a == n:
        answer = math.pow(a + 1, 2)
    else:
        answer = -1
    return answer

print(solution(121))