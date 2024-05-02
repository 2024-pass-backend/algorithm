def solution(n, left, right):
    answer = []
    l_block, l_idx = divmod(left, n)
    r_block, r_idx = divmod(right, n)
    # l_block == r_block
    if l_block == r_block:
        for i in range(l_idx, r_idx+1):
            if i <= l_block:
                answer.append(l_block+1)
            else:
                answer.append(i+1)
        return answer
    
    # left 블럭 생성
    left_list = []
    for i in range(l_idx, n):
        if i <= l_block:
            left_list.append(l_block+1)
        else:
            left_list.append(i+1)
    
    # right 블럭 생성
    right_list = []
    for j in range(r_idx+1):
        if j <= r_block:
            right_list.append(r_block+1)
        else:
            right_list.append(j+1)
    
    # 중간 블럭 생성
    mid_list = []
    for b in range(l_block+1, r_block):
        for i in range(n):
            if i<=b:
                mid_list.append(b+1)
            else:
                mid_list.append(i+1)
    answer = sum([left_list, mid_list, right_list], [])
    return answer