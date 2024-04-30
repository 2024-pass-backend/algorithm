from collections import deque
def solution(queue1, queue2):
    answer = -2
    length = len(queue1)
    que1 = deque(queue1)
    que2 = deque(queue2)
    
    sum1, sum2 = sum(que1), sum(que2)
    
    # target이 소수인 경우
    if (sum1+sum2)%2==1:
        return -1
    
    for i in range(length*4+1):
        if sum1==sum2:
            return i 
        
        if sum1>sum2:
            pop_n = que1.popleft()
            que2.append(pop_n)
            sum1 -= pop_n
            sum2 += pop_n
        elif sum1<sum2:
            pop_n = que2.popleft()
            que1.append(pop_n)
            sum1 += pop_n
            sum2 -= pop_n
        # print(i, '----')
        # print(sum1, que1)
        # print(sum2, que2)
        
    
    return -1