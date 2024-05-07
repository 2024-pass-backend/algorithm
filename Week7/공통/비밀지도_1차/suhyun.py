def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        aa = ''
        while arr1[i] > 0:
            aa += str(arr1[i] % 2)
            arr1[i] //= 2
        ss = ''
        if len(aa) < n:
            for s in range(n - len(aa)):
                ss += '0'
        aa = aa[::-1]
        a_ans = ss[:] + aa[:]
            

        bb = ''
        while arr2[i] > 0:
            bb += str(arr2[i] % 2)
            arr2[i] //= 2
        tt = ''
        if len(bb) < n:
            for s in range(n - len(bb)):
                tt += '0'
        bb = bb[::-1]
        b_ans = tt[:] + bb[:]
        
        ans = ['A'] * n
        for j in range(n):
            if a_ans[j] == '1' or b_ans[j] == '1':
                ans[j] = '#'
            else:
                ans[j] = ' '
        
        answer.append(''.join(ans))
            
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))