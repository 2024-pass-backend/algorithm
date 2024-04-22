def solution(a, b):
    answer = 0

    for i in range(len(a)):
        ans = a[i] * b[i]
        answer += ans
    return answer