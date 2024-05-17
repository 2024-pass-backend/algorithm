def solution(n):
    answer = []
    n = str(n)[::-1]
    print(n)
    print(list(map(int, n)))
    return list(map(int, n))
print(solution(12345))