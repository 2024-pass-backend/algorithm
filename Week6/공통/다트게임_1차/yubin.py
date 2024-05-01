def solution(dartResult):
    answer = []
    bonus = {'S':1, 'D':2, 'T':3}
    
    for i, s in enumerate(dartResult):
        # option
        if s=="*":
            answer[-1] *= 2
            if len(answer)>1:
                answer[-2] *= 2
        elif s=="#":
            answer[-1] *= -1
        
        # bonus
        elif s in bonus.keys():
            answer[-1] **= bonus[s]
        
        # score
        else:
            if s=='1' and dartResult[i+1]=='0':
                answer.append(10)
            elif s=='0' and dartResult[i-1]=='1':
                continue
            else:
                answer.append(int(s))
        # print(answer)
                
    return sum(answer)