# 10min
def solution(s):
    answer = []
    visited = set([])
    s = s.rstrip('}}').lstrip('{{').split('},{')
    ss = sorted(s, key=lambda x:len(x))
    for si in ss:
        si_list = list(map(int, si.split(',')))
        d = set(si_list)-visited
        answer.append(d.pop())
        visited = set(si_list)
    return answer