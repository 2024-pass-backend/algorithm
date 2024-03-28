import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
dict = {}
for x in a:
    if x in dict:
        dict[x] = dict[x] + 1
    else:
        dict[x] = 1

print(dict)

m = int(si())

for x in list(map(int, si().split())):
    if x in dict:
        print(dict[x], end=' ')
    else:
        print(0, end=' ')