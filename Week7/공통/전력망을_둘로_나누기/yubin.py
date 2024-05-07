from collections import defaultdict
def solution(n, wires):
    answer = 100
    graph = defaultdict(set)
    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    tree = defaultdict(set)
    visited = set([])

    while len(visited)<n-1:
        temp_dict = defaultdict(set)
        for k in range(1, n+1):
            if len(graph[k])==1:
                parent = graph[k].pop()
                visited.add(k)
                if parent not in tree[k]:
                    tree[parent].add(k)
                    temp_dict[parent].add(k)
                    for leaf in tree[k]:
                        tree[parent].add(leaf)

        for p in temp_dict.keys():
            graph[p] -= temp_dict[p]
        
    for t in tree.keys():
        answer = min(abs(n-2*len(tree[t])-2), answer)
        
    return answer