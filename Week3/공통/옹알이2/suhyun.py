# 10:16 ~ 10:26 
# 답지 풀이

def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:
        for c in can:
            if c * 2 not in bab:
                bab = bab.replace(c, ' ')
                print(bab)
        
        if bab.isspace():
            answer += 1
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))