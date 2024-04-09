
def bfs(visited, i, j, maps):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    queue = [[i, j]]
    visited[i][j] = True
    cnt = 0
    while queue:

        x, y = queue.pop(-1)
        cnt += int(maps[x][y])
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or visited[nx][ny] or maps[nx][ny] == "X":
                continue
            queue.append([nx, ny])
            visited[nx][ny] = True

    return cnt

def solution(maps):
    answer = []
    visited = [[False] * len(maps[i]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if visited[i][j] == False and maps[i][j] != "X":
                answer.append(bfs(visited, i, j, maps))
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer