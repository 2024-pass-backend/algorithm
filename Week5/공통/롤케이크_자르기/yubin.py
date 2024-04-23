from collections import defaultdict
def solution(topping):
    answer = 0
    set_front = set([])
    dic_back = defaultdict(list)
    n = len(topping)
    for i in range(1, n+1):
        dic_back[topping[n-i]].append(n-i)
        
    for j in range(n):
        set_front.add(topping[j])
        dic_back[topping[j]].pop()
        if len(dic_back[topping[j]])==0:
            del dic_back[topping[j]]
        # print(set_front)
        # print(dic_back)
        if len(set_front)==len(dic_back):
            answer += 1
        
    return answer