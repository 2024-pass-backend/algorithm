def solution(n):
    sqrt_n = n**0.5
    if sqrt_n%1:
        return -1
    answer = int(sqrt_n+1)**2
    return answer