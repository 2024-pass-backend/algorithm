def solution(elements):
    answer = set([])
    n = len(elements)
    for i in range(n):
        for length in range(1, n+1):
            if i+length <= n:
                answer.add(sum(elements[i:i+length]))
            else:
                temp = sum(elements[i:])+sum(elements[:length-(n-i)])
                answer.add(temp)
    # print(answer)
    return len(answer)