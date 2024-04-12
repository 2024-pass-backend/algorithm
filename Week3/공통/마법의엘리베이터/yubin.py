def solution(storey):
    answer = 0
    # 10^c 버튼
    max_c = len(str(storey))
    for c in range(1, max_c+2):
        if storey == 0:
            break
            
        now = storey%(10**c)//(10**(c-1))
        # print(now)
        # 5미만: 내려가기
        if now < 5:
            answer += now
            storey -= now*(10**(c-1))
            # print('down', storey)
        # 5초과: 10-now만큼 올라가기
        elif now > 5:
            answer += 10-now
            storey += (10-now)*(10**(c-1))
            # print('up', storey)
        # 5
        else:
            answer += 5
            # 앞 자리수가 5이상이면 올라가기
            if storey%(10**(c+1))//(10**c) >= 5:
                storey += 5*(10**(c-1))
            # 앞 자리수가 5미만이면 내려가기
            else:
                storey -= 5*(10**(c-1))
            # print('5', storey)
            
    return answer