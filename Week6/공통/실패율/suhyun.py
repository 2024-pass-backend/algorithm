# 저장해야할 사항은 크게 두가지
# 각 스테이지마다 클리어하지 못한 플레이어 수
# 스테이지에 도전한 사람

# 1 2 3 4 5 6 7 8
# 

def solution(N, stages):
    answer = []
    # 각 스테이지마다 클리어하지 못한 플레이어 수 -> 2십만
    a = dict() 
    for s in stages:
        if s == N + 1:
            s -= 1
        if s in a:
            a[s] += 1
        else:
            a[s] = 1
    
    # 스테이지에 도전한 사람
    ans = [0] * (len(stages) + 1)
    # 500 * 200000 = 10 * 7 
    for i in range(1, N+1):
        for s in stages:
            if i <= s:
                ans[i] += 1
    
    # a를 변경 -> 스테이지번호, 실패율
    for i in range(1, N+1):
        val = float(a[i]) / float(ans[i])
        a[i] = val
    
    print(a)
    aa = sorted(a.items(), key=lambda x: (-x[1], x[0]))
    print(aa)
    
    for key, value in aa:
        answer.append(key)
    
    return answer

stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5, stages))