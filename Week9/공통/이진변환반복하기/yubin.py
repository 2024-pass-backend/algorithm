def solution(s):
    answer = [0, 0]
    def find_zero(x):
        base_len = len(x)
        new_x = x.replace('0', '')
        c = len(new_x)
        num0 = base_len - c
        return_x = format(c, 'b')
        return num0, return_x
    while True:
        answer[0]+=1
        n0, s = find_zero(s)
        answer[1]+=n0
        if s=='1':
            break
    return answer