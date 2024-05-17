def solution(s):
    answer = [[] for _ in range(len(s.split(' ')))]
    idx = 0
    for elem in s.split(' '):
        for i, e in enumerate(elem):
            if i % 2 == 0:
                answer[idx].append(e.upper())
            else:
                answer[idx].append(e.lower())
        idx += 1

    ans = ''
    for arr in answer:
        ans += ''.join(arr)
        ans += ' '

    return ans[:-1]

print(solution("try hello world"))