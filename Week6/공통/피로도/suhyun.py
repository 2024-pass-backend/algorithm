# 내장함수 이용해서 해보자. -> permutations()
# from itertools import permutations
# repeat을 쓰는 것은 product뿐임!
# 8!
# 던전을 최대로 탐험하고 싶음.
from itertools import permutations
import math
answer = 0
d_len = 0

def solution(k, dungeons):
    global answer
    selected = [0] * len(dungeons) # 던전을 탐험하는 순서
    d_len = len(dungeons)
    
    for a in permutations(range(d_len), d_len):
        cnt = 0
        pe = k
        # print(a)
        for p in a:
            if dungeons[p][0] <= pe:
                pe -= dungeons[p][1]
                cnt += 1
        
        if answer < cnt:
            answer = cnt
        
    return answer

print(solution(80, 	[[80,20],[50,40],[30,10]]))