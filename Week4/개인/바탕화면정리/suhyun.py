def solution(wallpaper):
    answer = []
    
    sx, sy, ex, ey = len(wallpaper), len(wallpaper[0]), -1, -1
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                sx = min(sx, i)
                sy = min(sy, j)
                ex = max(ex, i)
                ey = max(ey, j)
    
    return [sx, sy, ex+1, ey+1]

print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))