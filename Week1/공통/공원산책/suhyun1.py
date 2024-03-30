x, y = 0, 0
dir = {"E" : (0,1), "S" : (1,0), "W" : (0,-1), "N" : (-1,0)}

def solution(park, routes):

    global x, y
    find_start(park)
    # print("최초 = " + str(x) + ", " + str(y))
    
    for route in routes:
        d, cnt = route.split()
        current_x, current_y = x, y
        # print(str(current_x) + ", " + str(current_y))
        for i in range(int(cnt)):
            nx, ny = x, y
            nx += dir[d][0]
            ny += dir[d][1]
            
            if nx >= 0 and ny >= 0 and nx < len(park) and ny < len(park[0]) and park[nx][ny] != "X":
                x += dir[d][0]
                y += dir[d][1]
            else:
                x = current_x
                y = current_y
                break
                
    return [x, y]


def find_start(park):
    global x, y
    for i, arr in enumerate(park):
        for j, elem in enumerate(arr):
            if park[i][j] == 'S':
                    x, y = i, j
                    return

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]	
print(solution(park, routes))