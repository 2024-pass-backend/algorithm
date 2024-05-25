# A: 65-90 a: 97-122
def solution(s, n):
    answer = []
    for i in range(len(s)):
        in_s = s[i]
        # 공백
        if in_s==' ':
            answer.append(in_s)
            continue
        
        s_ord = ord(in_s)
        st_i = 65 if s_ord<91 else 97
        s_ord -= st_i
        s_ord += n
        s_ord %= 26

        answer.append(chr(st_i+s_ord))
            
    return ''.join(answer)