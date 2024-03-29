import sys
si = sys.stdin.readline
k, n = map(int, si().split())
arr = [int(si().strip()) for _ in range(k)]

def determination(x):
    sum = 0
    for a in arr:
        if a >= x:
            sum += (a // x)
    return True if (sum >= n) else False

L, R, ans = 0, sys.maxsize, 0
while(L <= R):
    mid = (L + R) // 2
    if(determination(mid)):
        L = mid + 1
        ans = mid
    else:
        R = mid - 1

print(ans)