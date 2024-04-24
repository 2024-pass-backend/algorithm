# 3^17 	129140163
def solution(n):
    answer = 0
    three = []
    Flag=False
    for i in range(16, -1, -1):
        if n//(3**i)==0 and Flag==False:
            continue
        if n//(3**i)!=0:
            Flag = True
        three.append(n//(3**i))
        n %= (3**i)
    
    for j, t in enumerate(three):
        answer += t*(3**j)
            
    return answer