from itertools import combinations_with_replacement
def solution(n, info):
    diff = 0 # 점수 차
    answer = [-1]
    
    # 점수 계산
    def score_calculator(ryan):
        r_score, a_score = 0, 0
        for i in range(11):
            if ryan[i]>info[i]:
                r_score += 10-i
            elif info[i]>ryan[i]:
                a_score += 10-i
            elif info[i]:
                a_score += 10-i
        return r_score-a_score
    
    # 우승 방법 결정
    def select_win(origin, new):
        for i in range(11):
            if origin[10-i]>new[10-i]:
                return origin
            if origin[10-i]<new[10-i]:
                return new


    # 점수 얻어올 과녁 위치를 n개 고름
    comb = [i for i in range(11)]
    for target in combinations_with_replacement(comb, n):
        r_list = [0]*11
        for t in target:
            r_list[t] += 1

        now_diff = score_calculator(r_list)
        if now_diff>diff:
            answer = r_list
            diff = now_diff
        elif now_diff>0 and now_diff==diff:
            answer = select_win(answer, r_list)
    return answer