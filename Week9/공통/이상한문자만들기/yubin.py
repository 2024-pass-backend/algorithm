def solution(s):
    answer = []
    split_s = list(s.split(' '))
    for ss in split_s:
        a = ''
        for i, si in enumerate(ss):
            if i%2:
                a+=si.lower()
            else:
                a+=si.upper()
        answer.append(a)
    return ' '.join(answer)