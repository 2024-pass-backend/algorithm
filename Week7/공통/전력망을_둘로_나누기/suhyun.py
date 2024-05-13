# remove는 값으로 삭제한다.
# combinations는 중복을 허용하지 않으면서 뽑는 경우의 수를 의미한다.
# from itertools import combinations
from itertools import combinations
from collections import deque
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    
    # 그래프 완성
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for per in combinations(range(1, n+1), 2):
        v1, v2 = per
        visited = [False] * (n + 1)
        if v1 in graph[v2] and v2 in graph[v1]:
            graph[v2].remove(v1)
            graph[v1].remove(v2)
            # print(v1, v2)
            # print(graph)
            answer = min(answer, abs(bfs(v1, visited, graph) - bfs(v2, visited, graph)))
            # print(f'answer = {answer}')
            graph[v1].append(v2)
            graph[v2].append(v1)
    return answer

def bfs(n, visited, graph):
    dq = deque([n])
    cnt = 0
    while dq:
        v = dq.popleft()
        cnt += 1 
        visited[v] = True
        for vv in graph[v]:
            if not visited[vv]:
                dq.append(vv)
    return cnt

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))