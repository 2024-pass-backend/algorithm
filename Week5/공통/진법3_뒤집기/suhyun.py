def solution(n):
    answer = ''
    
    while(n >= 1):
        rest = n % 3
        n //= 3
        answer += str(rest)
    
    # answer를 3진수로 표현한후, 해당 answer를 10진수로 반환하라.
    return int(answer, 3)

print(solution(45))