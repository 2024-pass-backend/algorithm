def solution(numbers):
    answer = []
    for n in numbers:
        bit_n = format(n, 'b')
        bit_n = list(bit_n.zfill(len(bit_n)+1))
        for i in range(len(bit_n)):
            if bit_n[~i]=='0' and i==0:
                bit_n[~i] = '1'
                break
            if bit_n[~i]=='0' and i>0:
                bit_n[~i] = '1'
                bit_n[~i+1] = '0'
                break
        answer.append(int(''.join(bit_n), 2))
                
    return answer