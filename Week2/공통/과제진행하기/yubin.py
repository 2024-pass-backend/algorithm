def solution(plans):
    global answer, todo
    answer = []
    todo = []
    plans = sorted(plans, key=lambda x:x[1])
    
    for i in range(len(plans)):
        if i+1 == len(plans):
            next_plan = None
        else:
            next_plan = plans[i+1]
        process(plans[i], next_plan)
        
    while todo:
        process(todo.pop(), None)
    return answer

def process(now_list, next_list):
    # 다음 과제시간까지의 간격
    if next_list==None:
        term = float('inf')
    else:
        term = time_diff(now_list[1], next_list[1])
        
    play_time = int(now_list[2])
    remain_time = play_time - term
    if  remain_time> 0:
        now_list[2] = play_time-term
        todo.append(now_list)
    else:
        answer.append(now_list[0])
        if (remain_time<0) & len(todo)>0:
            now_time = time_add(now_list[1], play_time)
            todo[-1][1] = now_time
            process(todo.pop(), next_list)
    

def time_add(str_time, playtime):
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