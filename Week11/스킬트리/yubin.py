def solution(skill, skill_trees):
    answer = 0
    set_skill = set(skill)
    for st in skill_trees:
        temp = []
        for s in st:
            if s in set_skill:
                temp.append(s)
        
        if ''.join(temp)==skill[:len(temp)]:
            answer+=1
    return answer