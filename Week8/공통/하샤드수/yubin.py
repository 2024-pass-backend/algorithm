def solution(x):
    s = sum(map(int, list(str(x))))
    return x%s==0