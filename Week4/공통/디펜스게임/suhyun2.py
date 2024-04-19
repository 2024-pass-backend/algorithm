# 최대한 많은 라운드를 진행하기 위해서
# 적의 수가 많은 곳에다가 무적권을 사용하는게 좋음.
from queue import PriorityQueue

def solution(n, k, enemy):
    answer = 0
    pq = PriorityQueue()
    
    for e in enemy:
        if k > 0:
            pq.put(e)
            k -= 1
        else:
            # 현재의 적
            num = e
            
            if pq.queue[0] < num:
                num = pq.get()
                pq.put(e)
            
            if n >= num:
                n -= num
            else:
                break
        answer += 1
    return answer

enemy = [4, 2, 4, 5, 3, 3, 1]
print(solution(7, 3, enemy))