## 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값
## key = lambda x: x[] x[]
# 9:15 ~ 
def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x: [x[1], x[0]])
    
    before = 0
    # 첫번째 원소와 비교후, 두번째 원소로 갱신한다.
    for target in targets:
        if before <= target[0]:
            before = target[1]
            answer += 1
            
    
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))