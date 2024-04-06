# 9:44 ~ 
def solution(s):
    
    alpha = [-1] * 26
    answer = []
    
    for idx, alphabet in enumerate(s):
        if alpha[ord(alphabet) - 97] == -1:
            answer.append(-1)
        else:
            answer.append(idx - alpha[ord(alphabet) - 97])
        alpha[ord(alphabet) - 97] = idx
    return answer

print(solution("foobar"))