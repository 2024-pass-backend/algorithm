import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = list(map(int, si().split()))

def determination(x):
    sum = 0
    for e in a:
        if(e > x):
           sum += (e - x)
    
    if sum >= m:
        return True
    return False

L, R, ans = 0, 1000000000, 0
while(L <= R):
    mid = (L + R) // 2
    if(determination(mid)):
        ans = mid
        L = mid + 1
    else:
        R = mid - 1

print(ans)