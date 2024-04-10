# 3:46 ~ 
def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        for c in can:
            if not c * 2 in b:
                b = b.replace(c, ' ')
        
        if b.isspace():
            answer += 1
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))