# 4:31 ~ 5:05
# 점수차이가 같은 경우 어떻게 해야하는거지?
# 둘다 0점인 경우 count하면 안됨. -> 이 경우를 고려하지 않음
from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    ans = 0
    
    for a in combinations_with_replacement(range(11), n):
        info2 = [0] * 11
        for aa in a:
            info2[10-aa] += 1

        a1, a2 = 0, 0
        # 아! 어차피 낮은 점수부터 비교하기 때문에, 
        # 자동으로, 가장 낮은 점수를 더 많이 맞힌 경우가 return될듯!
        for i in range(11):
            if info[i] == info2[i] == 0:
                continue
            elif info[i] < info2[i]:
                a2 += (10 - i)
            else:
                a1 += (10 - i)
        if a1 < a2:
            gap = a2 - a1
            # 점수의 갭차가 크도록 해야하기때문에,
            # 단순히 라이언의 점수가 크다고 해서 바로 ans를 갱신하는 것은 안된다.
            if gap > ans:
                answer = info2
                ans = gap
        
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))