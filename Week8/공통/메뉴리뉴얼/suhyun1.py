# x = ['t', 'a', 'c]
# y = ['ac', 'b']
# x.append(y) > ['t', 'a' , 'c', ['ac', 'b']]
# x.extend(y) > ['t', 'a', 'c', 'ac', 'b']
# 딕셔너리에서 특정 키에 대한 값을 얻고자 할때 딕셔너리[키]로 해도되지만 딕셔너리.get(키)도 가능하다.
# 둘간의 차이점은 딕셔너리[키]로 할경우, 그 키가 없다면, 오류 반환
# 딕셔너리.get(키)로 할경우, 그 키가 없다면, None반환
from itertools import combinations
def solution(orders, course):
    answer = []
    
    for c in course:
        comb_count = {}
        order_comb = []
        max_order =[]
        for order in orders:
            order_comb = combinations(list(order), c)
            # print(order_comb)
            for order in order_comb:
                order_comb_str = ''.join(sorted(order))
                # print("order_comb_str = " + order_comb_str)
                
                if comb_count.get(order_comb_str):
                    comb_count[order_comb_str] += 1
                else:
                    comb_count[order_comb_str] = 1
        
        print(comb_count)
        max_order = [k for k,v in comb_count.items() if ((v == max(comb_count.values())) and v >= 2)]
        print(max_order)
        answer.extend(max_order)
        print(answer)
    
    answer = sorted(answer)
    return answer

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))