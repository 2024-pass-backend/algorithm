def solution(price, money, count):
    answer = -1
    
    sum_price = 0
    
    for c in range(1, count+1):
        sum_price += price * c
    
    # print(sum_price)
    if sum_price > money:
        return sum_price - money
    else: return 0

print(solution(3, 20, 4))