from itertools import combinations
def solution(orders, course):
    answer = []

    for c in course:
        comb_count = {}
        order_comb = []
        max_order = []
        for order in orders:
            order_comb = combinations(list(order), c)
            for order in order_comb:
                order_comb_str = ''.join(sorted(order))
                if comb_count.get(order_comb_str):
                    comb_count[order_comb_str] += 1
                else:
                    comb_count[order_comb_str] = 1

        max_order = [k for k,v in comb_count.items() if ((v == max(comb_count.values())) and v >= 2)]
        answer.extend(max_order)

    answer = sorted(answer)
    return answer

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))