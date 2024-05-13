t = int(input())
for tc in range(1, t+1):
    n = int(input())
    dir = [[0,1], [1,0], [0,-1], [-1,0]]
    arr = [[0] * n for _ in range(n)]
    start = 1
    x, y = 0, -1
    direction = 0
    while(start <= n * n):
        nx, ny = x + dir[direction][0], y + dir[direction][1]
        if (nx >= 0 and ny >= 0 and nx < n and ny < n and arr[nx][ny] == 0):
            arr[nx][ny] = start
            start += 1
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
    print(f'#{tc}')
    for row in arr:
        print(*row)
        
        