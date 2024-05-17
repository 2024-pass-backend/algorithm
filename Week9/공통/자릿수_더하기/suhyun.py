def solution(n):
    answer = 0

    for a in str(n):
        answer += int(a)

    return answer

print(solution(123))