# 3:06 ~ 3:40
def solution(a, b, n):
    answer = 0
    
    while (n // a) > 0:
        # 집에 두고 가는 병의 개수
        c = n - a * (n // a)
        # 마트에 가져간 후, 받는 병의 개수
        cnt = ((a * (n // a)) // a) * b
        answer += cnt
        n = c + cnt
    return answer

print(solution(3, 2, 20))