# 7분
def solution(keymap, targets):
    answer = []
    key_dic = {}
    for keymap_i in keymap:
        for i, key in enumerate(keymap_i):
            if key in key_dic.keys():
                key_dic[key] = min(key_dic[key], i+1)
            else:
                key_dic[key] = i+1
                
    for target in targets:
        temp = 0
        for t in target:
            if t in key_dic.keys():
                temp += key_dic[t]
            else:
                temp = -1
                break
        answer.append(temp)
    return answer