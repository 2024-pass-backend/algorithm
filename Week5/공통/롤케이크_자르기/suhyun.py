# 파이썬에서 set은 
# a = set([1, 2, 2])
# 형태로 선언한다.
# 요소를 추가하고 싶을 땐 a.add(원소)
# 요소가 a집합안에 포함되어있는지 확인할땐
# if 2 in a:
# 여러 요소를 추가하고 싶을땐 update()
# a.update([1,2,3])
# a.discard(원소) > a가 특정원소에 없을때 에러발생X
# a.remove(원소) > a가 특정원소에 없을때 에러발생
# 파이썬 집합의 크기 구할때 len

# https://velog.io/@k_bobin/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EB%A1%A4%EC%BC%80%EC%9D%B4%ED%81%AC-%EC%9E%90%EB%A5%B4%EA%B8%B0

from collections import Counter

def solution(topping):
    answer = 0
    old = Counter(topping)
    young = set()
    
    for i in topping:
        old[i] -= 1
        young.add(i)
        
        if old[i] == 0:
            old.pop(i)
        
        if len(old) == len(young):
            answer += 1
    
    return answer

topping = [1, 2, 1, 3, 1, 4, 1, 2]
# topping = [1, 2, 3, 1, 4]
print(solution(topping))