from queue import PriorityQueue
# from collections import deque

def solution(n, k, enemy):
    answer = 0
    pq = PriorityQueue()
    
    for e in enemy:
        if k > 0:
            pq.put(e)
            k -= 1
        else:
            num = e
            
            if pq.queue[0] < e:
                num = pq.get()
                pq.put(e)
        
            if n >= num:
                n -= num

        answer += 1

    return answer

enemy = [4, 2, 4, 5, 3, 3, 1]
print(solution(7, 3, enemy))