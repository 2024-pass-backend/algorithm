# 딕셔너리.keys()의 반환값은 리스트가 아니다.
import math
def getTime(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)

def solution(fees, records):
    answer = []
    #누적시간을 기록하는 해시맵
    time = dict()
    #들어오는 차량을 기록하는 해시맵
    in_list = dict()
    for re in records:
        t, num, a = re.split(" ")
        t = getTime(t)
        if a == "IN":
            in_list[num] = t
        elif a == "OUT":
            if num in in_list:
                if num in time:
                    time[num] = time[num] + (t - in_list[num])
                else:
                    time[num] = (t - in_list[num])
                del in_list[num]
    
    # print(time)
    # print(in_list)
    s = getTime("23:59")
    for n in in_list.keys():
        if n in time:
            time[n] = time[n] + (s - in_list[n])
        else:
            time[n] = s - in_list[n]
    
    nums = sorted(list(time.keys()))
    for n in nums:
        if time[n] > fees[0]:
            fee = fees[1] + ((math.ceil((time[n] - fees[0]) / fees[2])) * fees[3])
            answer.append(fee)
        else:
            answer.append(fees[1])
    return answer

# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]
# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees = [120, 0, 60, 591]
records = ["16:00 3961 IN", "17:00 2541 IN"]
print(solution(fees, records))