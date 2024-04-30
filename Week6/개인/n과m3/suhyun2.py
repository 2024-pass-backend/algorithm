# '구분자'.join(리스트)
n, m = map(int, input().split())
s = [0] * m

def pro(idx):
    if idx == m:
        print(' '.join(map(str, s)))
        return 
    else:
        for i in range(1, n+1):
            s[idx] = i
            pro(idx + 1)

pro(0)