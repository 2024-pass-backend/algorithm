from collections import deque


def solution(board):
    answer = -1
    n, m = len(board), len(board[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    q = deque()

    for x in range(n):
        for y in range(m):
            if board[x][y] == "R":
                sx, sy = x, y

    q.append((sx, sy, 0))

    while q:
        x, y, level = q.popleft()

        if board[x][y] == "G":
            answer = level
            break

        # 한방향으로 미끄러져 이동
        for dx, dy in direction:
            scope = 1
            while 1:
                nx, ny = x + dx * scope, y + dy * scope
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "D":
                    if visited[nx - dx][ny - dy] == False:
                        visited[nx - dx][ny - dy] = True
                        q.append((nx - dx, ny - dy, level + 1))

                    break
                scope += 1
    return answer