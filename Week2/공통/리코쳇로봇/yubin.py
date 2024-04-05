from collections import deque
def solution(board):
    h, w = len(board), len(board[0])
    
    Flag = False
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                rx, ry = j, i
                Flag = True
                break
        if Flag:
            break
    
    # 미끄러지기
    move_dic = {'down':(0, 1), 'up':(0, -1), 'left':(-1, 0), 'right':(1, 0)}
    def OoR(x, y):
        return (x<0) or (y<0) or (x>=w) or (y>=h)
    
    def slip(x, y, direction):
        tx, ty = x, y
        # 장애물 만나면 멈추기 + 범위 벗어나면 멈추기
        while (OoR(tx, ty)==False) and ((board[ty][tx] != 'D')):
            tx += move_dic[direction][0]
            ty += move_dic[direction][1]
        # 장애물/벽 만나기 직전 지점 return
        return tx-move_dic[direction][0], ty-move_dic[direction][1]
    
    def bfs(x, y):
        que = deque([(x, y)])
        visited = [[-1]*w for _ in range(h)]
        visited[y][x] += 1
        
        while que:
            nx, ny = que.popleft()
            for d in move_dic.keys():
                sx, sy = slip(nx, ny, d)
                if visited[sy][sx] > -1:
                    continue
                que.append((sx, sy))
                visited[sy][sx] = visited[ny][nx] + 1
                
                if board[sy][sx] == 'G':
                    for l in visited:
                        print(l)
                    return visited[sy][sx]
        return -1
    
    answer = bfs(rx, ry)

    return answer