def solution(arrayA, arrayB):
    answer, answer_a, answer_b = 0, 0, 0
    
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    
    #arrayA의 최대공약수 구하기
    a = arrayA[0]
    for i in range(1, len(arrayA)):
        a = gcd(a, arrayA[i])
        
    #arrayB의 최대공약수 구하기
    b = arrayB[0]
    for i in range(1, len(arrayB)):
        b = gcd(b, arrayB[i])
        
    # print(a, b) # 
    
    ## arrayA의 최대공약수가 arrayB에서 한번이라도 나누어 떨어지는지 확인
    aa_can = False
    for aa in arrayB:
        if aa % a == 0 :
            aa_can = True
            break
    
    ## arrayB의 최대공약수가 arrayA에서 한번이라도 나누어 떨어지는지 확인
    bb_can = False
    
    # print("b = " + str(b)) ## 
    
    for bb in arrayA:
        if bb % b == 0:
            bb_can = True
            break
    # print(bb_can) ## 
    
    if aa_can == False:
        answer_a = a
    if bb_can == False:
        answer_b = b
        
    # print(answer_a, answer_b)
    
    return max(answer_a, answer_b)

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

arrayA = [10, 17]
arrayB = [10, 17]
print(solution(arrayA, arrayB))