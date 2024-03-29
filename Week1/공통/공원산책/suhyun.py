def solution(park, routes):
    
    x, y = 0, 0
    dir = {"E":(0,1), "S":(1,0), "W":(0,-1), "N":(-1,0)}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i,j
                break
    
    for r in routes:
        d, n = r.split(' ')
        current_x, current_y = x, y
        
        for i in range(int(n)):
            nx = x + dir[d][0]
            ny = y + dir[d][1]
            
            if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]) or park[nx][ny] == "X":
                x, y = current_x, current_y
                break
            else:
                x = nx
                y = ny
    
    return (x, y)

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
print(solution(park, routes))