# 8:00 ~ 9:40 결국 못품
# 12:26 ~ 
# m - 가로, n - 세로
def solve(x, y, startX, startY, m, n):
    dist = []
    # 위쪽벽
    # 위쪽 벽에 맞았을 때, 목표의 y가 더 큰 경우, 공에 맞게 된다.
    if not (startX == x and startY < y):
        d = (startX - x) ** 2 + (startY - (n + (n - y))) ** 2
        dist.append(d)
    # 아래쪽벽
    # 아래쪽벽에 맞았을 때, 목표의 y가 더 작은 경우, 공에 맞게 된다.
    if not (startX == x and startY > y):
        d = (startX - x) ** 2 + (startY - (-y)) ** 2
        dist.append(d)
    # 오른쪽벽
    # 오른쪽벽에 맞았을 때, 목표의 x가 더 큰 경우, 공에 맞게 된다.
    if not (startY == y and startX < x):
        d = (startX - (m + (m - x))) ** 2 + (startY - y) ** 2
        dist.append(d)
    # 왼쪽벽
    # 왼쪽벽에 맞았을 때, 목표의 x가 더 작은 경우, 공에 맞게 된다.
    if not (startY == y and startX > x):
        d = (startX - (-x)) ** 2 + (startY - y) ** 2
        dist.append(d)

    return min(dist)

def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        x, y = ball
        answer.append(solve(x, y, startX, startY, m, n))
    return answer

balls = [[7, 7], [2, 7], [7, 3]]
print(solution(10, 10, 3, 7, balls))

