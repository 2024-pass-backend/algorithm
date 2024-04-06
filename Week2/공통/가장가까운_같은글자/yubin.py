def solution(s):
    answer = []
    alph_dic = {}
    for i, alph in enumerate(s):
        if alph not in alph_dic.keys():
            answer.append(-1)
            alph_dic[alph] = i
        else:
            answer.append(i-alph_dic[alph])
            alph_dic[alph] = i
        # print(i, alph)
    return answer