# 15:27~15:40~15:43
def solution(wallpaper):
    h = len(wallpaper)
    w = len(wallpaper[0])
    lux, luy, rdx, rdy = 52, 52, 0, 0
    
    for x in range(h):
        for y in range(w):
            if wallpaper[x][y] == '#':
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x)
                rdy = max(rdy, y)
            
    return [lux, luy, rdx+1, rdy+1]