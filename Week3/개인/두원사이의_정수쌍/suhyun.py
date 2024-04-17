# x=1부터 x=r2까지 점의 개수를 구한다.
# x=1부터 x=r1까지는 점의 개수가, r2에서 구한 점의 개수 - r1에서 구한 점의 개수가 된다.
import math

def solution(r1, r2):
    answer = 0
    
    for r in range(1, r2):
        if r < r1:
            answer += (getDotCnt(r, r2, "r2") - getDotCnt(r, r1, "r1"))
        else:
            answer += getDotCnt(r, r2, "r2")
    
    answer = answer * 4
    answer += (r2 - r1 + 1) * 4
    return answer

def getDotCnt(r, circle_r, s):
    y = math.sqrt(circle_r ** 2 - r ** 2)
    cnt_y = int(y)
    if s == "r1" and y == cnt_y:
        return cnt_y - 1
    return cnt_y

print(solution(2,3))