from collections import deque
def solution(cards):
    answer = 0
    graph = {i:card-1 for i, card in enumerate(cards)} # 카드도 0~n-1로 변환
    visited = [False] * len(cards)
    score = []
    
    def bfs(box_i, graph):
        cnt = 1
        que = deque([box_i])
        visited[box_i] = True
        while que:
            # print(que, visited)
            n = que.popleft()
            s = graph[n]
            if visited[s]:
                break
            que.append(s)
            visited[s] = True
            cnt += 1
        return cnt
    
    for i in range(len(cards)):
        if visited[i]==False:
            cnt = bfs(i, graph)
            score.append(cnt)
    # print(score)
    if len(score)>1:
        score.sort(reverse=True)
        answer = score[0]*score[1]
    return answer