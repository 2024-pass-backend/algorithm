def solution(price, money, count):
    total = (count+1)*(count//2)
    if count%2==1:
        total += (count+1)/2
    answer = total*price-money

    return answer if answer>0 else 0