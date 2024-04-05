def solution(plans):
    answer = []
    # 분 단위로 변경
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1][:2])*60 + int(plans[i][1][3:])
        plans[i][2] = int(plans[i][2])
    # 시작 시간 기준 정렬
    plans.sort(key=lambda x: x[1])
    
    stack = []
    for idx in range(len(plans)-1):
        stack.append([plans[idx][0], plans[idx][2]])
        gap = plans[idx+1][1] - plans[idx][1]
        while (len(stack)>0) & (gap>0):
            if stack[-1][1] <= gap:
                name, playtime = stack.pop()
                answer.append(name)
                gap -= playtime
            else:
                stack[-1][1] -= gap
                gap = 0
    
    answer.append(plans[-1][0])
    for _ in range(len(stack)):
        answer.append(stack.pop()[0])
            
    return answer