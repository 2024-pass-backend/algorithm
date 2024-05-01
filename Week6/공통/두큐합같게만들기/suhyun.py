from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    limit = len(q1) * 3 
    # q1의 원소가 q2로 모두 이동하는 경우
    # q2의 원소가 q1으로 모두 이동하는 경우
    # 남은 q2의 원소가 q1으로 이동하는 경우
    
    while sum1 != sum2:
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
        answer += 1

        # 두 큐를 모두 왕복했는데도 반복문이 돈다면, 
        # 같게 만들 수 없는 경우이다.
        if answer == limit:
            return -1
        
    return answer

print(solution([3,2,7,2], [4, 6, 5, 1]))