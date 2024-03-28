## 자바 Integer.MAX_VALUE -> sys.maxsize
import sys
si = sys.stdin.readline
n, s = map(int, si().split())
arr = list(map(int, si().split()))

R, sum, ans = 0, 0, sys.maxsize
for L in range(0, len(arr)):
    while(sum < s and R < n):
        sum += arr[R]
        R += 1
    
    if(sum >= s):
        ans = min(ans, R - L)
        sum -= arr[L]

print(0 if ans == sys.maxsize else ans)