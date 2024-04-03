from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for g in goal:
        if (len(cards1) > 0) & (len(cards2) > 0):
            if g == cards1[0]:
                cards1.popleft()
            elif g == cards2[0]:
                cards2.popleft()
            else:
                return 'No'
        elif len(cards1) > 0:
            if g == cards1[0]:
                cards1.popleft()
            else:
                return 'No'
        elif len(cards2) > 0:
            if g == cards2[0]:
                cards2.popleft()
            else:
                return 'No'
        else:
            return 'No'
    
    return 'Yes'