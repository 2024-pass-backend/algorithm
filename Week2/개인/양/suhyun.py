import sys
si = sys.stdin.readline
dir = [[0,1], [1,0], [0,-1], [-1,0]]
v_cnt, o_cnt, v_ans, o_ans = 0, 0, 0, 0

def dfs(x, y):
    visited[x][y] = True
    global v_cnt, o_cnt
    if adj[x][y] == 'v':
        v_cnt += 1
    elif adj[x][y] == 'o':
        o_cnt += 1
        
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if adj[nx][ny] != '#' and not visited[nx][ny]:
            dfs(nx, ny)

r, c = map(int, si().split())
visited = [[False] * c for _ in range(r)]
adj = [si().strip() for _ in range(r)] ## 2차원 배열로 하지 않고, 1차원배열로 한 후, 각 인덱스마다 입력받은 것을 한번에 저장
for i in range(r):
    for j, elem in enumerate(adj[i]):
        if elem != '#' and not visited[i][j]:
            dfs(i, j)
            print(i, j, v_cnt, o_cnt)
            if v_cnt >= o_cnt:
                if (v_cnt == 0 and o_cnt == 0):
                    continue
                v_ans += v_cnt
            else:
                if (v_cnt == 0 and o_cnt == 0):
                    continue
                o_ans += o_cnt
            v_cnt, o_cnt = 0, 0
print('-----')
print(o_ans, v_ans)