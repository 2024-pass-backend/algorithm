def solution(numbers):
    answer = []
    
    # for n in range(1, 11):
    #     print(bin(n)[2:])
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            a = '0' + bin(n)[2:]
            # print(a)
            right_zero_idx = a.rfind('0')
            t = list(a)
            t[right_zero_idx] = '1'
            t[right_zero_idx + 1] = '0'
            
            ans_str = ''.join(t)
            
            ans = int(ans_str, 2)
            answer.append(ans)
    return answer

print(solution([7]))