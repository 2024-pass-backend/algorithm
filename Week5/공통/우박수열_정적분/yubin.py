def solution(k, ranges):
    answer = []
    ice = [k]
    range_area = []
    while k>1:
        if k%2==0: 
            k//=2
        else: 
            k = k*3+1
        ice.append(k)
        if len(ice)>1:
            range_area.append((ice[-1]+ice[-2])/2)
    # print(ice)
    # print(range_area)
    for a, b in ranges:
        area = 0
        if b<=0:
            b = len(ice)-1+b
        # print(a, b)
        if a>b:
            area = -1
        else:
            for i in range(a, b):
                area+= range_area[i]
        answer.append(area)

    return answer