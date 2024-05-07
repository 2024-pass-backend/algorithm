def solution(d, budget):
    d = sorted(d, reverse=True)
    # print(d)
    while sum(d) > budget:
        d = d[1:]
    return len(d)

print(solution([1,3,2,5,4], 9))