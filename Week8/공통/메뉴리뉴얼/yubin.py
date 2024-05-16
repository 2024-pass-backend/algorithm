from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    menu = {i:defaultdict(int) for i in range(2, 11)}
    for o in orders:
        sorted_o = ''.join(sorted(list(o)))
        for l in range(2, min(len(o)+1, 11)):
            cb = combinations(sorted_o, l)
            for c in cb:
                menu[l][c]+=1

    for c in course:
        re_menu = defaultdict(list)
        for k, v in menu[c].items():
            if v>1:
                re_menu[v].append(''.join(k))

        if re_menu:
            answer.append(re_menu[max(re_menu.keys())])
            
    answer = sum(answer, [])
    return sorted(answer)