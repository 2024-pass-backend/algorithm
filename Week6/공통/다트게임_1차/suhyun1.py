def solution(dartResult):
    answer = 0
    
    n = ''
    score = []
    for d in dartResult:
        if d.isnumeric():
            n += d
        elif d == 'S':
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif d == 'D':
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif d == 'T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif d == '#':
            score[-1] = -score[-1]
        elif d == '*':
            if len(score) > 1:
                score[-1] = score[-1] * 2
                score[-2] = score[-2] * 2
            else:
                score[-1] = score[-1] * 2
    
    return sum(score)

print(solution("1D2S#10S"))