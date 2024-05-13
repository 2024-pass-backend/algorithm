from itertools import combinations
def calculation(eq1, eq2):
    x1, y1, c1 = eq1
    x2, y2, c2 = eq2
    
    if x1 * y2 == y1 * x2:
        return
    
    x = (y1*c2 - c1*y2) / (x1*y2 - y1 * x2)
    y = (c1 * x2- x1 * c2) / (x1*y2 - y1*x2)
    
    if x == int(x) and y == int(y):
        return [int(x), int(y)]

def solution(line):
    answer = []
    points = []
    for eq1, eq2 in combinations(line, 2):
        point = calculation(eq1, eq2)
        if point:
            points.append(point)
    
    # 그림의 시작점과 마지막점 찾기
    print(points)
    w1, w2 = min(points, key=lambda x:x[0])[0], max(points, key=lambda x:x[0])[0] + 1
    h1, h2 = min(points, key=lambda x:x[1])[1], max(points, key=lambda x:x[1])[1] + 1
    print(w1, w2, h1, h2)
    
    answer = [['.'] * (w2 - w1) for _ in range(h2- h1)]
    
    for x, y in points:
        answer[y-h1][x-w1] = '*'
    # print([''.join(a) for a in answer])
    answer.reverse()
    return [''.join(a) for a in answer]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))