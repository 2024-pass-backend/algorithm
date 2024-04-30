# 배열.pop(index)
# 배열.remove(원소)
def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    for r in reserve:
        c1 = r - 1
        c2 = r + 1
        if c1 in lost:
            lost.remove(c1)
        elif c2 in lost:
            lost.remove(c2)
    
#     print(lost)
    return n-len(lost)

print(solution(5, [2,4], [1,3,5]))