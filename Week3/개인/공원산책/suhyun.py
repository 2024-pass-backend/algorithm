# 8:00 ~ 8:16
sx, sy = 0, 0

dir = {"E":(0,1), "S":(1,0), "W":(0,-1), "N":(-1,0)}

def solution(park, routes):
    
    for i, row in enumerate(park):
        for j, col in enumerate(row):
            if col == 'S':
                sx, sy = i, j
    print(sx, sy)
    print("시작")
    
    for route in routes:
        d, cnt = route.split(" ") # E 2
        nx, ny = sx, sy
        for i in range(int(cnt)):
            x, y = dir[d]
            nx += x # 0 
            ny += y # 2
            # print("nx = " + str(nx) + ", ny = " + str(ny))
            if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]) or park[nx][ny] == 'X':
                nx, ny = sx, sy
                # print("탔음")
                break
        sx = nx
        sy = ny
            
    return [sx, sy]

park = ["OSO","OOO","OXO","OOO"]
# park = ["SOO","OXX","OOO"]
routes = ["E 2","S 3","W 1"]
# routes = ["E 2","S 2","W 1"]
print(solution(park, routes))