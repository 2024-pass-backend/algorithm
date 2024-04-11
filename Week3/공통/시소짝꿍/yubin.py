from collections import defaultdict
from itertools import combinations
import math
def solution(weights):
    answer = 0
    pair = defaultdict(list) # key:토크 value:몸무게
    same = defaultdict(int)
    for w in weights:
        same[w] += 1
        if same[w] > 1:
            continue
        pair[w*2].append(w)
        pair[w*3].append(w)
        pair[w*4].append(w)
    
    for s_w in same.values():
        if s_w>1:
            answer += math.comb(s_w, 2)
    for pair_w in pair.values():
        if len(pair_w)>1:
            for pw1, pw2 in combinations(pair_w, 2):
                answer += same[pw1]*same[pw2]
        
    return answer

