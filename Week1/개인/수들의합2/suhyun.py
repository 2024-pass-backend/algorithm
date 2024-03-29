import sys
si = sys.stdin.readline
n, m = map(int, si().split())
arr = list(map(int, si().split()))

R, sum, ans, cnt = 0, 0, sys.maxsize, 0
for L in range(n):
    while(R < n and sum < m):
        sum += arr[R]
        R += 1
    
    if(sum >= m):
        if (sum == m):
            cnt += 1
        ans = min(ans, R - L)
        sum -= arr[L]

print(cnt)