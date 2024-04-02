def solution(plans):
    answer = []
    stack = []

    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])  # 시작시간 기준 정렬

    for i in range(len(plans) - 1):
        stack.append([plans[i][0], plans[i][2]])
        gap = plans[i + 1][1] - plans[i][1]
        while stack and gap:
            if stack[-1][1] <= gap:  # 남은 playtime<=gap
                cn, ct = stack.pop()  # 다 풀었으니 제거
                gap -= ct
                answer.append(cn)
            else:  # 시간안에 못푼다면
                stack[-1][1] -= gap  # 남은 시간 남겨둠
                gap = 0

    answer.append(plans[-1][0])
    for i in range(len(stack)):
        answer.append(stack[~i][0])  # 정수 i에 대해 ~i는 -i-1과 동일합니다==리스트의 끝에서 i번째 위치에 있는 요소의 첫 번째 아이템을 참조
    return answer