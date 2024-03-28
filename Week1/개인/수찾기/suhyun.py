import sys
si = sys.stdin.readline

def binary_search(a, l, r, x):
    while(l <= r):
        mid = (l + r) // 2
        if a[mid] > x:
            r = mid - 1
        elif a[mid] < x:
            l = mid + 1
        else:
            return True
    return False
            

n = int(si())
a = list(map(int, input().split()))
a.sort()
m = int(si())
for x in list(map(int, input().split())):
    print(1 if binary_search(a, 0, len(a) - 1, x) else 0)
    
