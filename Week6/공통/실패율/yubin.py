from collections import defaultdict
def solution(N, stages):
    answer = []
    total_user = len(stages)
    
    # 스테이지 별 멈춘 유저 수 저장
    stage_user = defaultdict(int)
    for s in stages:
        stage_user[s] += 1
    
    fail_dict = defaultdict(int)
    for stage in range(1, N+1):
        if total_user == 0:
            fail_dict[stage] = 0
        else:
            fail_dict[stage] = stage_user[stage]/total_user
            total_user -= stage_user[stage]
    
    # print(fail_dict)
    fail = dict(sorted(fail_dict.items(), key=lambda x: x[1], reverse=True))
    # print(fail.keys())
    
    return list(fail.keys())