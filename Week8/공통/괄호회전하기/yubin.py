from collections import deque
def solution(s):
    if len(s)%2==1:
        return 0
    
    def correct_str(ss):
        n = len(ss)
        for _ in range(n//2):
            ss = ss.replace('()', '')
            ss = ss.replace('[]', '')
            ss = ss.replace('{}', '')
            if ss=='':
                return 1
        return 0
    
    answer = correct_str(s)
    
    que_s = deque(list(s))
    for i in range(len(s)-1):
        que_s.rotate(-1)
        rotate_s = ''.join(que_s)
        answer+=correct_str(rotate_s)
    return answer