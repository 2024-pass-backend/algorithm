def solution(park, routes):
    H = len(park)
    W = len(park[0])
    
    # 공원 이탈
    def OoR(x, y):
        return x<0 or y<0 or x>=W or y>=H
    # 장애물
    def Obstacle(x, y):
        return park[y][x]=="X"
    # 이동
    move_dic = {"N":(0, -1),
               "S":(0, 1),
               "W":(-1, 0),
               "E":(1, 0)}
    def move(x, y, route):
        nx, ny = x, y
        direction = route[0]
        distance = int(route[-1])
        for _ in range(distance):
            dx, dy = move_dic[direction]
            nx += dx
            ny += dy
            if OoR(nx, ny) or Obstacle(nx, ny):
                return x, y
        return nx, ny
    Flag = False
    for y in range(H):
        for x in range(W):
            if park[y][x] == "S":
                Flag = True
                break
        if Flag: break
    
    for route in routes:
        x, y = move(x, y, route)
    answer = [y, x]
    return answer