# 배열.remove(값)
# remove의 파라미터는 인덱스가 아니다!
def solution(n, lost, reserve):
    answer = n
    
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    reserve.sort()
    lost.sort()
    
    for r in reserve[:]:
        for l in lost:
            if l == r - 1:
                reserve.remove(r)
                lost.remove(l)
                break
            elif l == r + 1:
                reserve.remove(r)
                lost.remove(l)
                break

    return answer - len(lost)

print(solution(5, [2,4], [1,3,5]))