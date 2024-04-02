def solution(plans):
    answer = []
    plans = sorted(plans, key=lambda x:x[1])
    temp = []
    plan_dic = {name:[start, int(playtime)] for name, start, playtime in plans}
    
    for i in range(len(plans)):
        plan_name = plans[i][0]
        end_time = time_cal(plan_dic[plan_name][0], plan_dic[plan_name][1])
        # print(plan_name, end_time)
        
        if i<len(plans)-1:
            if end_time < plans[i+1][1]:
                answer.append(plan_name)
                remain_time = time_diff(plans[i+1][1], end_time)
                if temp:
                    while remain_time:
                        p_n = temp.pop()
                        plan_dic[p_n][1] -= remain_time
                        if plan_dic[p_n][1] > 0:
                            remain_time = 0
                            temp.append(p_n)
                        elif plan_dic[p_n][1] == 0:
                            remain_time = 0
                            answer.append(p_n)
                        else:
                            remain_time = abs(plan_dic[p_n][1])
            elif end_time == plans[i+1][1]: 
                answer.append(plan_name)
            else:
                temp.append(plan_name)
                play_time = time_diff(end_time, plans[i+1][1])
                plan_dic[plan_name][1] -= play_time
        else:
            answer.append(plan_name)
            
    while temp:
        p_n = temp.pop()
        answer.append(p_n)
                                                 
    return answer

def time_cal(str_time, playtime):
    h, m = int(str_time[:2]), int(str_time[-2:])
    m += playtime
    
    while m>=60:
        h += 1
        m -= 60
    return f"{h:02d}:{m:02d}"

def time_diff(small, big):
    s_h, s_m = int(small[:2]), int(small[-2:])
    b_h, b_m = int(big[:2]), int(big[-2:])
    
    return (b_h*60+b_m)-(s_h*60+s_m)