def solution(grid):
    h, w = len(grid), len(grid[0])
    coord = [[0]*(3*w+1) for _ in range(3*h+1)]
    loc = set([])
    # grid 넣기
    for r in range(3*h+1):
        for c in range(3*w+1):
            if r%3==0 and c%3==0:
                coord[r][c] = -1
            elif r%3!=0 and c%3!=0:
                coord[r][c] = grid[r//3][c//3]
            else:
                loc.add((r, c))
    # print(loc)
    # 빛 진입 방향
    def light_direc(r, c):
        if r%3==1:
            return 'right'
        if r%3==2:
            return 'left'
        if c%3==1:
            return 'up'
        if c%3==2:
            return 'down'

    # 빛 이동
    grid_dic = {'right':{'g':[0, 1], 'S':[0, 2], 'L':[-1, 0], 'R':[2, 1]}, 
                'left':{'g':[0, -1], 'S':[0, -2], 'L':[1, 0], 'R':[-2, -1]}, 
                'up':{'g':[-1, 0], 'S':[-2, 0], 'L':[0, -1], 'R':[-1, 2]}, 
                'down':{'g':[1, 0], 'S':[2, 0], 'L':[0, 1], 'R':[1, -2]}}
    def light_move(r, c):
        d = light_direc(r, c)
        g = [r+grid_dic[d]['g'][0], c+grid_dic[d]['g'][1]]
        g_d = coord[g[0]][g[1]]
        m = [g[0]+grid_dic[d][g_d][0], g[1]+grid_dic[d][g_d][1]]
        return m
    
    # 공간 내에서 이동
    def control_range(r, c):
        if r==3*h and c%3==2:
            return (0, c)
        if r==0 and c%3==1:
            return (3*h, c)
        if c==3*w and r%3==1:
            return (r, 0)
        if c==0 and r%3==2:
            return (r, 3*w)
        return (r, c)

    answer = []  
    while loc:
        nr, nc = loc.pop()
        coord[nr][nc] = 1
        nr, nc = control_range(nr, nc)
        if (nr, nc) in loc:
            loc.remove((nr, nc))
            coord[nr][nc] = 1
        sr, sc = light_move(nr, nc)

        while coord[sr][sc]!=1:
            loc.remove((sr, sc))
            coord[sr][sc] = coord[nr][nc]+1
            sr, sc = control_range(sr, sc)
            if (sr, sc) in loc:
                loc.remove((sr, sc))
            if coord[sr][sc]==1:
                break
            coord[sr][sc] = coord[nr][nc]+1

            nr, nc = sr, sc
            sr, sc = light_move(nr, nc)
        answer.append(coord[nr][nc])

    return sorted(answer)
        

