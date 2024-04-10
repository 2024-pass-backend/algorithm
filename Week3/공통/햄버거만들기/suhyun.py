#9:08 ~ 9:58 -> 왜 시간초과가 나는거지?
# [2, 1, 2, 3, 1, 2, 3, 1]
# [1, 3, 2, 1, 2, 1, 3, 1, 2]

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	통과 (69.41ms, 10.2MB)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	실패 (시간 초과)
# 테스트 13 〉	통과 (0.00ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.1MB)
# 테스트 17 〉	통과 (0.00ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)

def solution(ingredient):
    answer = 0
    
    while True:
        can_make = False
        for i, elem in enumerate(ingredient):
            cnt = 0
            if elem == 1 and i + 4 <= len(ingredient):
                if ingredient[i] == 1 and ingredient[i+1] == 2 and ingredient[i+2] == 3 and ingredient[i+3] == 1:
                    while cnt < 4:
                        ingredient.pop(i)
                        cnt += 1
                    can_make = True
                    answer += 1
                    break
        
        if can_make == False:
            break       
    
    return answer

# ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
ingredient = [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))