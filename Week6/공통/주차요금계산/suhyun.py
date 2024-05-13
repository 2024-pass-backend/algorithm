# https://wikidocs.net/16 -> 딕셔너리로 원소 삭제
# del 딕셔너리[삭제하려는 키] -> O(1)
import math
def getCalculate(t, fees): # 이때 t는 출차 - 입차 (소요시간)
    if t <= fees[0]:
        return fees[1]
    else:
        return fees[1] + (math.ceil((t - fees[0]) / fees[2])) * fees[3] 

def getTime(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def solution(fees, records):
    answer = []
    r = dict() # key = 차량이름, value = 시간, 입차/출차
    ans = dict() # key = 차량이름 value = [총 주차시간, 돈]
    
    for rr in records:
        car = list(rr.split(' '))
        if car[2] == "IN":
            time = getTime(car[0])
            r[car[1]] = [time, car[2]]
        elif car[2] == "OUT":
            if car[1] in r:
                out_time = getTime(car[0])
                money = getCalculate(out_time - r[car[1]][0], fees)
                if car[1] in ans:
                    ans[car[1]] = [(out_time - r[car[1]][0]) + ans[car[1]][0], money]
                else:
                    ans[car[1]] = [out_time - r[car[1]][0], money]
                del r[car[1]]
    
    # 입차만 하고 출차한 경우
    for dummy_car in r:
        out_time = getTime("23:59")
        if dummy_car in ans:
            money = getCalculate((out_time - r[dummy_car][0]) + ans[dummy_car][0], fees)
            ans[dummy_car] = [out_time - r[dummy_car][0], money]
        else:
            money = getCalculate((out_time - r[dummy_car][0]), fees)
            ans[dummy_car] = [out_time - r[dummy_car][0], money]
    
    a = sorted(ans, key=lambda x:x)
    for k in a:
        answer.append(ans[k][1])
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))