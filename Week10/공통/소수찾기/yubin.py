def solution(n):
    def isPrime(num):
        if num==1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    answer = []
    for i in range(2, n+1):
        isprime = True
        if len(answer)==0:
            answer.append(i)
            continue
        for j in answer:
            if j>int(n**0.5):
                break 
            if i%j==0:
                isprime = False
                break
        if isprime:
            answer.append(i)
        
    return len(answer)