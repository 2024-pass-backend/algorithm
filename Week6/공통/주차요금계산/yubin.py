import math
def solution(fees, records):
    answer = []
    record_dic = dict()
    for r_idx in range(len(records)):
        time, car, status = records[~r_idx].split()
        if status=='OUT':
            if int(car) not in record_dic.keys():
                record_dic[int(car)] = int(time[:2])*60+int(time[3:])
            else:
                record_dic[int(car)] += int(time[:2])*60+int(time[3:])
        elif status=='IN':
            if int(car) in record_dic.keys():
                record_dic[int(car)] -= int(time[:2])*60+int(time[3:])
            else:
                record_dic[int(car)] = 23*60+59 - (int(time[:2])*60+int(time[3:]))
    
    # print(record_dic)
    for car_num in sorted(record_dic.keys()):
        add_time = record_dic[car_num]-fees[0]
        if add_time<=0:
            answer.append(fees[1])
        else:
            cost = fees[1] + math.ceil(add_time/fees[2])*fees[3]
            answer.append(cost)
    return answer