from itertools import combinations_with_replacement
def solution(n, info):
    max_gap = -1 #점수 차 
    answer = [-1]
    
    # 중복 조합으로 0~10점까지 n개 뽑기
    for combi in combinations_with_replacement(range(11), n):
        info2 = [0] * 11 # 라이언의 과녁점수
        
        for i in combi: # 0~10점까지 n개뽑은 n개를 모두 라이언의 과녁점수에 넣기
            info2[10-i] += 1
        
        apeach, lion = 0,0
        for idx in range(11):
            # 라이언과 어피치 모두 한번도 화살을 맞히지 못한 경우
            if info[idx] == info2[idx] == 0:
                continue
            # 어피치가 라이언이 쏜 화살의 수 이상을 맞힌 경우
            elif info[idx] >= info2[idx]:
                apeach += 10 - idx
            # 라이언이 어피치가 쏜 화살의 수 이상을 맞힌 경우
            else:
                lion += 10 - idx
        
        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
            