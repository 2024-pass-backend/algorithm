def solution(n):
    list_n=list(str(n))
    s_n = sorted(list_n, reverse=True)
    return int(''.join(s_n))