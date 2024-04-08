# 10:14 ~ 10:20
import math
def solution(number, limit, power):
    answer = 0
    a = []
    
    for i in range(1, number+1):
        end = math.sqrt(i)
        # 4면 루트2 -> 루트2까지 포함하여 약수의 개수를 센다.
        cnt = 0
        for k in range(1, int(end) + 1):
            if i % k == 0:
                if k == end:
                    cnt += 1
                else: 
                    cnt += 2    
        a.append(cnt)
    
    # print(a)
    for aa in a:
        if aa > limit:
            answer += power
        else:
            answer += aa
    return answer

print(solution(10, 3, 2))