import math
def solution(w,h):
    a=0
    l, s = max(h,w), min(h, w)
    if w==h:
            a = w
    else :
        for i in range(1,s+1):
            a += (math.ceil(l*i/s) - math.floor(l*(i-1)/s))
    answer = w*h - a
    return answer