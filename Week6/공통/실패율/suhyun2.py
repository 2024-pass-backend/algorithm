# stages = [2, 1, 2, 6, 2, 4, 3, 3], N -> 5
def solution(N, stages):
    answer = []
    
    #실패율
    ratio = {}
    allPlayer = len(stages)
    
    for i in range(1, N+1):
        if allPlayer == 0:
            ratio[i] = 0
        else:
            ratio[i] = stages.count(i) / allPlayer
            allPlayer -= stages.count(i)
    
    answer = sorted(ratio, key=lambda x:ratio[x], reverse=True)
    
    return answer

stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5, stages))