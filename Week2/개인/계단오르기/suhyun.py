import sys
si = sys.stdin.readline
n = int(si())
d = [0] * 301
stairs = [0] * 301

for i in range(1, n+1):
    stairs[i] = int(si())

d[1] = stairs[1]
d[2] = stairs[1] + stairs[2]
d[3] = max(stairs[1], stairs[2]) + stairs[3]
for i in range(4, n+1):
    d[i] = max(d[i - 3] + stairs[i - 1], d[i - 2]) + stairs[i]

print(d[n])
    
    