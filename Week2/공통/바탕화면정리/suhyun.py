def solution(wallpaper):
    startX, startY, endX, endY = len(wallpaper), len(wallpaper[0]), -1, -1
    
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                startX = min(i, startX)
                endX = max(i, endX)
                startY = min(j, startY)
                endY = max(j, endY)
    
    # print(startX, startY, endX + 1, endY + 1)
                
    
    return [startX, startY, endX + 1, endY + 1]