def solution(n, l, r):
    return cnt_one(r, n) - cnt_one(l-1, n)

def cnt_one(idx, depth):
    if idx==0:
        return 0
    if depth == 0:
        return 1
    
    m, r = divmod(idx, 5**(depth-1))

    if m==5:
        ones = 4**depth
    elif m>2:
        ones = 4**(depth-1)*(m-1)
    elif m>0:
        ones = 4**(depth-1)*m
        if m == 2:
            r = 0
    else:
        ones = 0
    
    return ones + cnt_one(r, depth-1)