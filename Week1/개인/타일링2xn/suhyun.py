import sys
si = sys.stdin.readline
n = int(si())
d = [0] * 1001

d[1] = 1
d[2] = 2
d[3] = 3

for i in range(4, len(d)):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])