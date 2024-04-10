#9:08 ~ 9:42 -> 왜 시간초과가 나는거지? 그리고 히든테케에서 실패가 뜸.
# [2, 1, 2, 3, 1, 2, 3, 1]
# [1, 3, 2, 1, 2, 1, 3, 1, 2]

def solution(ingredient):
    answer = 0
    
    while True:
        can_make = False
        for i, elem in enumerate(ingredient):
            cnt = 0
            if elem == 1 and i + 4 <= len(ingredient):
                if ingredient[i] == 1 and ingredient[i+1] == 2 and ingredient[i+2] == 3 and ingredient[i+3] == 1:
                    print("처음")
                    print(ingredient)
                    while cnt < 4:
                        print("i = " + str(i))
                        ingredient.pop(i)
                        cnt += 1
                        print(ingredient)
                    can_make = True
                    print("============")
                    print(ingredient)
                    answer += 1
                    break
        
        if can_make == False:
            break       
    
    return answer

# ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
ingredient = [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))