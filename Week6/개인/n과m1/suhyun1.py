import sys
si = sys.stdin.readline
n, m = map(int, si().split())
visited = [False] * (n+1)
selected = [0] * m

def pro(idx):
    if idx == m:
        print(' '.join(map(str, selected)))
        return
    else:
        for i in range(1, n+1):
            if visited[i] == False:
                visited[i] = True
                selected[idx] = i
                pro(idx + 1)
                visited[i] = False

pro(0)