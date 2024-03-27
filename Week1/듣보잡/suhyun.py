# 문자열.strip() - 좌우 공백 제거
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = set()
ans = []
for i in range(n):
    a.add(si().strip())

for i in range(m):
    name = si().strip()
    if name in a:
        ans.append(name)

ans.sort()

print(ans)
print(a)

for x in ans:
    print(x)        