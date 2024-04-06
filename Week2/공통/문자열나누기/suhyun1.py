def solution(s):
    answer = 0
    cnt1, cnt2 = 0, 0
    
    for i in s:
        if cnt1 == cnt2:
            k = i
            answer += 1
        
        if k == i:
            cnt1 += 1
        else:
            cnt2 += 1
    return answer

print(solution("abracadabra"))
# print(solution("aaabbaccccabba"))