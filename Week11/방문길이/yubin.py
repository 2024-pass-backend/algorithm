def solution(dirs):
    answer = 0
    
    def OoR(x, y):
        return abs(x)>5 or abs(y)>5
    move = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    grid_dic = {}
    for i in range(-5, 6):
        for j in range(-5, 6):
            tem_dic = {}
            for dx, dy in move.values():
                nx, ny = i+dx, j+dy
                if OoR(nx, ny):
                    continue
                tem_dic[(nx, ny)]=0
            grid_dic[(i, j)]=tem_dic
            
    nx, ny = 0, 0
    for dir in dirs:
        dx, dy = move[dir]
        sx, sy = nx+dx, ny+dy
        if OoR(sx, sy):
            continue
            
        if grid_dic[(nx, ny)][(sx, sy)]==0:
            answer += 1
            grid_dic[(nx, ny)][(sx, sy)] += 1
            grid_dic[(sx, sy)][(nx, ny)] += 1
        nx, ny = sx, sy
    return answer