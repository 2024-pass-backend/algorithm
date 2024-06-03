def solution(s):
    answer = sorted(list(s), key=lambda x: -ord(x))
    return ''.join(answer)