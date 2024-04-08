# 9:40 ~ 10:00
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    start = 0
    b = True
    a = []
    while True:
        for i in range(start, start+m):
            if(i < len(score)):
                a.append(score[i])
                # print(a)
            else:
                b = False
                break
        
        # print(a)
        if b == False:
            break
        answer += a[m-1] * m
        start += m
        a = []
        
    return answer

score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
# [4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 1, 1]
print(solution(4, 3, score))