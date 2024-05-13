# 12:51 ~ 
# 문자열이 리스트에 담긴다. list(문자열)
from collections import deque
def solution(s):
    answer = 0
    ss = list(s)
    a = deque(ss)
    b = deque(ss)
    while True:
        if check(a):
            answer += 1
        if a:
            s = a.popleft()
            a.append(s)
        if a == b:
            break
    return answer

def check(aa):
    check_not = True
    b = deque(aa)
    a = []
    while b:
        if b[0] in ['(', '{', '[']:
            a.append(b[0])
            b.popleft()
        elif b[0] in [')', ']', '}']:
            if a:
                if b[0] == ')' and a[-1] == '(':
                    a.pop()
                    b.popleft()
                elif b[0] == ']' and a[-1] == '[':
                    a.pop()
                    b.popleft()
                elif b[0] == '}' and a[-1] == '{':
                    a.pop()
                    b.popleft()
                else:
                    check_not = False
                    break
            else:
                check_not = False
                break
    return check_not

print(solution("(){{"))