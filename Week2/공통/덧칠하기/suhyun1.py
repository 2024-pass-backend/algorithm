# end_painted - s + 1 = m
# section에서 원소들을 차례로 꺼내, 꺼낸 원소부터 색칠할 수 있는 마지막 구간까지 칠한다고 가정한다.
def solution(n, m, section):
    answer, end_painted = 0, 0
    for s in section:
        # 이미 칠한 구간은 포함시키지 않고, 칠하지 않았다면, 다시 꺼낸 원소부터 칠할 수 있는 구간까지 칠한다.
        if s > end_painted:
            end_painted = m + s - 1
            answer += 1
    return answer