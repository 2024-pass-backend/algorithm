from itertools import combinations
def solution(number):
    answer = 0
    for three in combinations(number,3):
        if sum(three)==0:
            answer+=1
    return answer