from collections import deque
def solution(order):
    answer = 0
    order = deque(order)
    add_belt = []
    for box in range(1, len(order)+1):
        while len(add_belt)>0 and order[0]==add_belt[-1]:
            answer += 1
            add_belt.pop()
            order.popleft()
        if box==order[0]:
            answer += 1
            order.popleft()
        else:
            add_belt.append(box)
    while len(add_belt)>0 and order[0]==add_belt[-1]:
        answer += 1
        add_belt.pop()
        order.popleft()
    return answer