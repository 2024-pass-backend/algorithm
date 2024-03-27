## 파이썬에서 boolean타입이 false인경우, 이를 참으로 만들기 위해 not visited[i]라고 작성한다.
## !visited[i] 가 아님!
import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
a.sort()
ans = 0
target = int(si())

def binary_search(a, l, r, x):
    while(l <= r):
        mid = (l + r) // 2
        if a[mid] < x:
            l = mid + 1
        elif a[mid] > x:
            r = mid - 1
        else:
            return True
    return False

for i in range(len(a)):
    if binary_search(a, 0, len(a) - 1, target - a[i]):
        ans += 1

print(ans // 2)