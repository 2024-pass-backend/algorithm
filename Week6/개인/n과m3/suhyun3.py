from itertools import product
n, m = map(int, input().split())
selected = [0] * m

def pro(idx):
    if idx == m:
        print(' '.join(map(str, selected)))
    else:
        for i in range(1, n+1):
            selected[idx] = i
            pro(idx + 1)
pro(0)