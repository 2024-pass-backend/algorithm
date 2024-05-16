from collections import defaultdict
def solution(info, query):
    answer = []
    
    language = {'cpp':set(), 'java':set(), 'python':set()}
    job = {'backend':set(), 'frontend':set()}
    career = {'junior':set(), 'senior':set()}
    food = {'chicken':set(), 'pizza':set()}
    score = []
    for idx, i in enumerate(info):
        l, j, c, f, s = i.split()
        language[l].add(idx)
        job[j].add(idx)
        career[c].add(idx)
        food[f].add(idx)
        score.append(int(s))

    for q in query:
        q_list = q.split() # l:0, j:2, c:4, f:6, s:7
        res_set = set([i for i, s in enumerate(score) if s>=int(q_list[-1])])
            
        if q_list[0]!='-':
            temp = set([])
            for r in res_set:
                if r in language[q_list[0]]:
                    temp.add(r)
            res_set = temp

        if q_list[2]!='-':
            temp = set([])
            for r in res_set:
                if r in job[q_list[2]]:
                    temp.add(r)
            res_set = temp

        if q_list[4]!='-':
            temp = set([])
            for r in res_set:
                if r in career[q_list[4]]:
                    temp.add(r)
            res_set = temp

        if q_list[6]!='-':
            temp = set([])
            for r in res_set:
                if r in food[q_list[6]]:
                    temp.add(r)
            res_set = temp

        answer.append(len(res_set))
        
    return answer