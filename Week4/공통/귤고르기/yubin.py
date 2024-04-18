from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    t_dic = defaultdict(int)
    for t in tangerine:
        t_dic[t] += 1
    
    tan = sorted(list(t_dic.values()))
    box = tan.pop()
    answer = 1
    while box<k:
        box+=tan.pop()
        answer += 1
    return answer