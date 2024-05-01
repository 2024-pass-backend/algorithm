# Counter(리스트)
# {1:4, 2:3}와 같은 형식으로 변함 
# 딕셔너리에서 원소를 제거하는 방법은 2가지이다.
# del 딕셔너리[키]
# 딕셔너리.pop(키) -> pop을 사용하면 해당 키를 제거할때, 그 키에 해당하는 value를 반환한다.
from collections import Counter
def solution(topping):
    answer = 0
    old = Counter(topping)
    young = set()
    
    for t in topping:
        old[t] -= 1
        young.add(t)
        
        if old[t] == 0:
            del old[t]
        if len(old) == len(young):
            answer += 1 
    
    return answer

topping = [1, 2, 1, 3, 1, 4, 1, 2]
# topping = [1, 2, 3, 1, 4]
print(solution(topping))