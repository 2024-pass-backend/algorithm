# 문자열 뒤집기
# 문자열[::-1]
import math
def isPrime(x):
    if int(x) == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(int(x))) + 1):
            if int(x) % i == 0:
                return False
        return True

def k_num(n,k):
    if k == 10:
        return n
    else:
        new_n = ''
        while n > 0:
            new_n += str(n % k)
            n //= k
        return new_n[::-1]

def solution(n, k):
    answer = 0
    num = k_num(n,k)
    # print(num)
    nums = str(num).split("0")
    print(nums)
    
    for x in nums:
        if x and isPrime(x):
            answer += 1
        
    return answer

print(solution(437674, 3))