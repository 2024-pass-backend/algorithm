import math
def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        cnt, s = 0, 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0 and (i * i != n):
               cnt += 1
            if i * i == n:
                s += 1
        cnt *= 2
        cnt += s

        if cnt % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer

print(solution(13, 17))