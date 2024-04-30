import sys
si = sys.stdin.readline
n, m = map(int, si().split())
selected = [0] * m

def pro(idx):
    if idx == m:
        print(' '.join(map(str, selected)))
        return
    else:
        if idx == 0:
            start = 1
        else:
            start = selected[idx - 1]
        for i in range(start, n+1):
            selected[idx] = i
            pro(idx + 1)
            

pro(0)