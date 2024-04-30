from itertools import combinations
n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
answer = list(combinations(numbers, m))
for e in answer:
    print(' '.join(map(str, e)))
