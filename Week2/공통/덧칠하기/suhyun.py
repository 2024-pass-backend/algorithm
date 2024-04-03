# 14 ~ 
# m = n_painted - s + 1
# m + s - 1 = n_painted
# section에 꺼낸 원소를 기준으로 어디까지 칠할 수 있는지 판단한다.
# 그 이후 다음 원소를 꺼낼때 이미 칠했는지 판단한다.
def solution(n, m, section):
    n_painted, answer = 0, 0
    for s in section:
        if s > n_painted:
            n_painted = s + m - 1
            answer += 1
    return answer