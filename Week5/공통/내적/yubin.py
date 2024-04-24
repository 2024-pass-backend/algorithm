def solution(a, b):
    answer = 0
    for ai, bi in zip(a, b):
        answer += ai*bi
    return answer