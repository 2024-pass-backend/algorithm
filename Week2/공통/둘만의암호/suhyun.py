alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def solution(s, skip, index):
    answer = ''
    for c in s:
        count = 0
        c_idx = alpha.index(c)
        while count < index:
            c_idx += 1
            if c_idx > 25:
                c_idx %= 26
            if alpha[c_idx] not in skip:
                count += 1
        answer += alpha[c_idx]
    return answer

s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))