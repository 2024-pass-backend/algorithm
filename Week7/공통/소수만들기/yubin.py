from itertools import combinations
def solution(nums):
    answer = 0
    
    def isPrime(n):
        if n==1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True
        
    cb = combinations(nums, 3)
    for three in cb:
        s = sum(three)
        if isPrime(s):
            answer += 1

    return answer