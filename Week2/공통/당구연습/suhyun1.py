# m은 가로길이, n은 세로길이
def solve(m, n, startX, startY, x, y):
    dist = []
    if not(startX < x and startY == y):
        distance = (startX - (m + (m - x))) ** 2 + (startY - y) ** 2
        dist.append(distance)
    
    if not(startX > x and startY == y):
        distance = (startX - (-x)) ** 2 + (startY - y) ** 2
        dist.append(distance)
    
    if not(startX == x and startY < y):
        distance = (startX - x) ** 2 + (startY - (n + (n - y))) ** 2
        dist.append(distance)
        
    if not(startX == x and startY > y):
        distance = (startX - x) ** 2 + (startY - (-y)) ** 2
        dist.append(distance)
    
    return min(dist)

def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        answer.append(solve(m, n, startX, startY, x, y))
    
    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))