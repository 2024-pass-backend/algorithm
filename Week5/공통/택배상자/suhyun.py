from collections import deque
def solution(order):
    order = deque(order)
    stack = []
    result = [] #트럭에 실은 상자
    for i in range(1, len(order) + 1):
        stack.append(i)
        while stack:
            if stack and stack[-1] == order[0]:
                num = order.popleft()
                stack.pop()
                result.append(num)
            else:
                break
    return len(result)

print(solution([4, 3, 1, 2, 5]))