from itertools import product
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
case = product(range(1, n+1), repeat=m)
# for i in case:
#     for j in i:
#         print(j, end=' ')
#     print()
for i in case:
    print(' '.join(map(str, i)))