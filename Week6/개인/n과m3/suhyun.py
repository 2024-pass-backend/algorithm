# 내장함수 이용하는 경우
from itertools import product
n, m  = map(int, input().split())
case = product(range(1, n+1), repeat=m)

for i in case:
    for j in i:
        print(j, end=" ")
    print()