def solution(storey):
    answer = 0
    str_storey = str(storey)
    # 일의 자리 수는 별도 계산
    for i in range(len(str_storey)-1):
        now_num = int(str_storey[i])
        # 현재 내려갈 예정
        if now_num > 5:
            answer += 10-now_num
            # 만약 앞에서 하나 더 못 더하면 지금 더 해주기 
            if i==0:
                answer += 1
            # 뒷 자리에서도 내려갈 예정
            if int(str_storey[i+1])>5:
                answer -= 1 # 하나 덜 내려가기
        # 현재는 올라갈 예정
        else:
            answer += now_num
            # 뒷자리에서 내려갈 예정
            if int(str_storey[i+1])>5:
                answer += 1
        
    # 일의 자리
    last_num = int(str_storey[-1])
    # 5보다 크면 내려오기
    if last_num>5:
        answer += 10-last_num
    # 5 같거나 작으면 올라가기
    else:
        answer += last_num
    return answer