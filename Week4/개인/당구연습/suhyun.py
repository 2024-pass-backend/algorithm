import math
def pro(x, y, m, n, startX, startY):
    #위
    ans = []
    if not (y > startY and x == startX):
        d = ((n + (n - y)) - startY) * ((n + (n - y)) - startY) + (startX - x) * (startX - x)
        ans.append(d)
    #아래
    if not (y < startY and x == startX):
        d = (-y - startY) * (-y - startY) + (startX - x) * (startX - x)
        ans.append(d)
    #오른쪽
    if not (y == startY and x > startX):
        d = (y - startY) * (y - startY) + ((m + (m-x)) - startX) * ((m + (m-x)) - startX)
        ans.append(d)
    #왼쪽
    if not (y == startY and x < startX):
        d = (y - startY) * (y - startY) + (-x - startX) * (-x - startX)
        ans.append(d)
    return min(ans)

def solution(m, n, startX, startY, balls):
    answer = []
    for b in balls:
        answer.append(pro(b[0], b[1], m, n, startX, startY))
    return answer

balls = [[5,8]]
print(solution(10, 10, 5, 9, balls))