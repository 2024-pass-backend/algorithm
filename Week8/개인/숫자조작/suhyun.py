from itertools import combinations
tc = int(input())
for t in range(1, tc+1):
    aa = input()
    n = list(aa)
    max_val, min_val = 0, 1e9
    # 무조건 한번 교환해본다.
    for per in combinations(range(0, len(n)), 2):
        # print(per)
        temp_a = n[per[0]]
        temp_b = n[per[1]]
        n[per[1]] = temp_a
        n[per[0]] = temp_b
        num = ''.join(n)
        print(num)
        if num[0] == '0':
            n = list(aa)
            continue
        else:
            num = int(num)
            max_val = max(max_val, num)
            min_val = min(min_val, num)
        n = list(aa)
    if min_val == 1e9 and max_val == 0:
        min_val, max_val = int(aa), int(aa)
    # 원래 숫자가 더 큰 경우
    if max_val < int(aa):
        max_val = int(aa)
    if min_val > int(aa):
        min_val = int(aa)
    print(f'#{t} {min_val} {max_val}')
        