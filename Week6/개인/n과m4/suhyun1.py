from itertools import combinations_with_replacement
n, m = map(int, input().split())
answers = list(combinations_with_replacement(range(1, n+1), m))
for e in answers:
    print(' '.join(map(str, e)))