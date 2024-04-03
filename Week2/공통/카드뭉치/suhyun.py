def solution(cards1, cards2, goal):
    answer = ''
    ans = False
    card1, card2 = -1, -1
    for g in goal:
        ans = False
        for i, c in enumerate(cards1):
            if c == g and card1 + 1 == i:
                card1 = i
                ans = True
        
        for i, c in enumerate(cards2):
            if c == g and card2 + 1 == i:
                card2 = i
                ans = True
        
        if ans == False:
            answer = "No"
            break
    
    if ans == True:
        answer = "Yes"
    return answer

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))