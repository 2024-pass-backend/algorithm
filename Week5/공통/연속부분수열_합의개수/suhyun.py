from collections import deque
def solution(elements):
    answer = set()
    elements = deque(elements)
    for j in range(len(elements)):
        k = elements.popleft()
        elements.append(k)
        for i in range(1,len(elements)):
            # print(list(elements)[:i])
            answer.add(sum(list(elements)[:i]))
    answer.add(sum(elements))
    return len(answer)

print(solution([7,9,1,1,4]))