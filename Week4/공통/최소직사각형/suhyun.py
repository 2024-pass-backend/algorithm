# 명함을 회전시킬 수 있기때문에 가로와 세로는 서로 바뀔 수 있다.
# 가로 세로 길이중 큰 값들 중 최댓값을 찾고
# 가로 세로 길이중 작은 값들 중 최댓값을 찾아
# 위 두개를 곱한다.
def solution(sizes):
    w = []
    h = []
    
    for size in sizes:
        if size[0] > size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            w.append(size[1])
            h.append(size[0])
    
    return max(w) * max(h)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))