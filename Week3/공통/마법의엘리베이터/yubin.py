def solution(storey):
    answer = 0
    max_c = len(str(storey))
    for _ in range(max_c+1):
        now = storey % 10
        if (now > 5) or (now==5 and storey//10%10 >= 5):
            answer += (10-now)
            storey += (10-now)
        else:
            answer += now
        storey //= 10
    return answer