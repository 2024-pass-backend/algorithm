# https://yjg-lab.tistory.com/398 이 블로그보고 문제 이해함
group = []
def solution(cards):
    answer = 0
    visited = [False] * len(cards)
    for start in range(len(cards)):
        selected = [start + 1]
        if visited[start] == False:
            visited[start] = True
            dfs(cards, selected, visited, start, cards[start])
            group.append(selected)
    
    print(group)
    a1, a2 = 0, 0
    idx1, idx2 = 0, 0
    v_group = [False] * len(group)
    for i, g in enumerate(group):
        if len(g) > a1:
            if v_group[i] == False:
                a1 = len(g)
                idx1 = i
                v_group[i] = True
    # print(a1)
    # print(idx1)
    v_group = [False] * len(group)
    v_group[idx1] = True
    for i, g in enumerate(group):
        if len(g) > a2:
            if v_group[i] == False:
                a2 = len(g)
                idx2 = i
                v_group[i] = True
    print(a2)
    return a1 * a2

def dfs(cards, selected, visited, start, num):
    next_num = cards[num - 1] # 4 7 1
    if visited[num-1] == False:
        visited[num-1] = True
        selected.append(next_num)
        dfs(cards, selected, visited, start, next_num)
    else:
        selected[-1] = cards[num - 1]
        
print(solution([8,6,3,7,2,5,1,4]))