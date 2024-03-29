def solution(park, routes):
    x, y = 0, 0
    w, h = len(park[0]), len(park)
    op = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    # 시작점
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j
                break

    for r in routes:
        d, n = r.split(" ")  # 방향, 횟수
        dx, dy = x, y #현재 방향을 저장해야함 만약 갈수없다면 뒤로 돌아옴
        for i in range(int(n)):
            # 이동할 위치
            nx = x + op[d][0]
            ny = y + op[d][1]

            if 0 <= nx <= h - 1 and 0 <= ny <= w - 1 and (park[nx][ny] != "X"):
                x, y = nx, ny

            else:
                x, y = dx, dy
                break
    ## x,y 반환

    return (x, y)
