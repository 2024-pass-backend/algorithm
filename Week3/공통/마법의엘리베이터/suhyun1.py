def solution(storey):
    answer = 0
    
    while storey:
        remainder = storey % 10 # 각 자리를 보기 위함
        if remainder > 5:
            answer += (10 - remainder) # +1
            storey += 10
        elif remainder < 5:
            answer += remainder
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10
    return answer

print(solution(16))