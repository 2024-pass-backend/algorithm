from itertools import permutations
def solution(k, dungeons):
    answer = -1
    
    for permu_dungeons in permutations(dungeons):
        now_pow = k
        temp = 0
        for min_pow, use_pow in permu_dungeons:
            if now_pow < min_pow:
                break
            now_pow -= use_pow
            temp += 1
        
        if temp == len(dungeons):
            return len(dungeons)
        if answer < temp:
            answer = temp
    
    return answer