# 배열.sort(key=len)
# 8:00 ~ 8:37
def solution(s):
    answer = []
    s = s[1:-1]
    array = s.split("},{")
    array.sort(key=len)
    new_set = set()
    new_array = []
    for arr in array:
        num = ''
        for a in arr:
            if a == ',':
                if int(num) not in new_set:
                    new_set.add(int(num))
                    new_array.append(int(num))
                num = ''
            if a == "{" or a == "}" or a == ',':
                continue
            num += a
        if len(num) > 0 and int(num) not in new_set:
            new_set.add(int(num))
            new_array.append(int(num))
    return new_array

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{123}}"))