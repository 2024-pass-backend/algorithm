def solution(s):
    answer = 0
    alph_dic = {'other':0}
    for alph in s:
        if len(alph_dic)==1:
            alph_dic[alph] = 1
            continue
        if alph in alph_dic.keys():
            alph_dic[alph] += 1
        else:
            alph_dic['other'] += 1
        
        if list(alph_dic.values())[0] == list(alph_dic.values())[1]:
            answer += 1
            alph_dic = {'other':0}
    if len(alph_dic)>1:
        answer += 1
    return answer