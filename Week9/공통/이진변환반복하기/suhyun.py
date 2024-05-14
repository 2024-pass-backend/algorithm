# 1:53 ~ 2:01
def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    while(s != '1'):
        zero_cnt += s.count('0')
        ans = []
        for a in list(s):
            if a == '1':
                ans.append(a)
        aa = ''.join(ans)
        s = bin(len(aa))[2:]
        cnt += 1
    return [cnt, zero_cnt]

print(solution("110010101001"))