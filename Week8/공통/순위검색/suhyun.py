def solution(info, query):
    answer = []
    infos = dict()
    lan = dict()
    sta = dict() # {'backend': [], 'frontend': []}
    year = dict()
    food = dict()
    score = dict()
    language = ['java', 'python', 'cpp']
    stack = ['backend', 'frontend']
    years = ['junior', 'senior']
    foods = ['pizza', 'chicken']
    
    for l in language:
        lan[l] = []
    for s in stack:
        sta[s] = []
    for y in years:
        year[y] = []
    for f in foods:
        food[f] = []
    
    for i in info:
        per = i.split(" ")
        l = i.strip(per[0]).strip()
        s = i.strip(per[1]).strip()
        y = i.strip(per[2]).strip()
        f = i.strip(per[3]).strip()
        if i in infos:
            infos[i] += 1
        else:
            infos[i] = 1
        lan[per[0]].append(l)
        sta[per[1]].append(s)
        year[per[2]].append(y)
        food[per[3]].append(f)
        if per[4] in score:
            score[per[4]] += 1
        else:
            score[per[4]] = 1

    for q in query:
        print(q)
        person = ''.join(q.split('and | and|and '))
        print(person)
        print(person[6])
        if '-' in person:
            cnt = 0
            for idx, pp in person:
                if idx == 0:
                    for infos in lan[pp]:
                        for n in person.strip(pp):
                            if n in infos:
                                cnt += 1                                
                elif idx == 1:
                    for infos in sta[pp]:
                        for n in person.strip(pp):
                            if n in infos:
                                cnt += 1
                elif idx == 2:
                    for infos in year[pp]:
                            for n in person.strip(pp):
                                if n in infos:
                                    cnt += 1
                elif idx == 3:
                    for infos in food[pp]:
                            for n in person.strip(pp):
                                if n in infos:
                                    cnt += 1
                else:
                    if pp in score:
                        cnt += score[pp] 
            answer.append(cnt)       
        else:
            answer.append(infos[person])
                
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))