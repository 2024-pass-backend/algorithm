def solution(keymap, targets):
    answer = []

    for target in targets: #ABCD
        sum = 0
        for t in target: #A
            cnt = 101
            for key in keymap:
                if t in key:
                    cnt = min(cnt, key.find(t))
                    # print(cnt + 1)
            if cnt == 101:
                sum = -1
                break
            sum += (cnt + 1)
        answer.append(sum)

    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
print(solution(keymap, targets))