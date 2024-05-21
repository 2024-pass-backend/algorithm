def solution(n):
    answer = list(str(n))
    a = list(map(int, reversed(answer)))
    return a