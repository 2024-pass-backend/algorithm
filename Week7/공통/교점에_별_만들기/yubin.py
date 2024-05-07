from itertools import combinations
from collections import defaultdict
def solution(line):
    cb = combinations(line, 2)
    
    x_range = []
    y_range = []
    star = defaultdict(set)
    for two in cb:
        a, b, e = two[0]
        c, d, f = two[1]
        
        under = a*d-b*c
        if under==0:
            continue
        # 정수 확인
        x = (b*f-e*d)/under
        y = (e*c-a*f)/under
        if x%1==0 and y%1==0:
            star[int(y)].add(int(x))
            # 저장 없음
            if len(x_range)==0 and len(y_range)==0:
                x_range = [x, x]
                y_range = [y, y]
            # 저장 업데이트
            x_range[0] = int(min(x_range[0], x))
            x_range[1] = int(max(x_range[1], x))
            y_range[0] = int(min(y_range[0], y))
            y_range[1] = int(max(y_range[1], y))

    
    answer = []
    
    xr = x_range[1]-x_range[0]+1
    
    for yi in range(y_range[1], y_range[0]-1, -1):
        row = ["."]*xr
        for xi in star[yi]:
            row[xi-x_range[0]]="*"
        answer.append(''.join(row))
    return answer