# 9:10 ~ 9:19, 10:01 ~
from collections import deque

## 시작시간의 "h:m" 형태를 h * 60 + m 형태로 바꾼다. 그리고 걸린시간을 int로 바꾼다.
## 시작시간을 기준으로 정렬한다.
def init(plans):
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x:x[1])
    
def solution(plans):
    answer = []
    stack = []
    
    init(plans)
    queue = deque(plans)
    
    while queue:
        name, start, time = queue.popleft()
        current_time = 0
        if queue:
            next_name, next_start, next_time = queue[0]
        
        if queue:
            # 제 시간안에 작업을 끝낼 수 있는 경우
            if(start + time <= next_start):
                answer.append(name)
                current_time = start + time
                while stack:
                    remain_name, remain_time = stack.pop()
                    # 남은 작업을 다음 작업의 시작시각 전까지 끝낼 수 있는 경우
                    if current_time + remain_time <= next_start:
                        answer.append(remain_name)
                        current_time += remain_time
                    else:
                        stack.append([remain_name, remain_time - (next_start - current_time)])
                        break
            # 제 시간안에 작업을 끝내지 못하는 경우
            else:
                stack.append([name, time - (next_start - start)])
        else:
            answer.append(name)
            while stack:
                remain_name, remain_time = stack.pop()
                answer.append(remain_name)      
    return answer

plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))