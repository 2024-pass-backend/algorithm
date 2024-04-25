from collections import deque
def solution(want, number, discount):
    answer = 0
    want_dic = {w:0 for w in want}
    ten = deque(discount[:10])
    for t in ten:
        if t in want_dic.keys():
            want_dic[t] += 1
    if list(want_dic.values())==number:
        answer += 1
            
    for i in range(10, len(discount)):
        # 맨 앞 제거
        temp = ten.popleft()
        if temp in want_dic.keys():
            want_dic[temp] -= 1
        # 새 원소 추가
        new = discount[i]
        ten.append(new)
        if new in want_dic.keys():
            want_dic[new] += 1
        # 원하는 제품추가 체크
        if list(want_dic.values())==number:
            answer += 1
        
    return answer