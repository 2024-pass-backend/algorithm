def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    total = int(n*(n+1)/2)
    print(total)
    layer = 0
    num = 1
    while num<total:
        # left
        for k in range(layer*2, n-1-layer):
            answer[k][layer] = num
            num += 1
        # floor
        for k in range(layer, n-2*(layer+1)+1):
            answer[n-1-layer][k] = num
            num += 1
        # right
        for k in range(n-1-layer, 2*layer, -1):
            answer[k][-(layer+1)] = num
            num += 1
        layer += 1
    if num == total:
        answer[2*layer][layer] = num
    
        
    return sum(answer, [])