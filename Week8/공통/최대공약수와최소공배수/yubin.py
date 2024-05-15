import math
def solution(n, m):
    g = math.gcd(n, m)
    l = n*m//g
    return [g,l]