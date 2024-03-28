# 스스로 구현
def solution(sequence, k):
    L = 0
    R = len(sequence)-1
    
    LeftPlus = True
    
    while True:
        sum_LR = sum(sequence[L:R+1])

        if sum_LR==k:
            # print('k')
            return [L, R]
        
        if (L != R) & (sequence[L]==sequence[R]):
            R = L + int(k / sequence[L]) - 1
            # print('LR')
            return [L, R]
        
        if sum_LR < k:
            R -= 1
            LeftPlus = False
            if R < L:
                L = R
                
        if LeftPlus:
            L += 1
        else:
            L -= 1
        # print(L, R)

# 답안 참고 후 다시 푼 것
def solution(sequence, k):
    answer = [0, len(sequence)]
    L, R = 0, 0
    sum_LR = sequence[0]
    
    while True:
        if sum_LR < k:
            R += 1
            if R == len(sequence):
                break
            sum_LR += sequence[R]
        else:
            if sum_LR == k:
                if R-L < answer[1] - answer[0]:
                    answer = [L, R]
            sum_LR -= sequence[L]
            L += 1
    
    return answer
            