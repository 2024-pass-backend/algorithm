def solution(picks, minerals):
    answer = 0
    stress_dic = {'diamond':[1, 5, 25], 'iron':[1, 1, 5], 'stone':[1, 1, 1]} # key: 광물, value: 곡괭이 피로도
    stress = []
    for i in range(0, len(minerals), 5):
        temp = [0, 0, 0]
        for m in minerals[i:i+5]:
            temp[0] += stress_dic[m][0]
            temp[1] += stress_dic[m][1]
            temp[2] += stress_dic[m][2]
        stress.append(temp)
        
    if len(stress) > sum(picks):
        stress = stress[:sum(picks)]
    stress = sorted(stress, key=lambda x:x[2], reverse= True)
    
    s_idx = 0
    Flag = False
    for p_idx, p in enumerate(picks):
        for _ in range(p):
            answer += stress[s_idx][p_idx]
            s_idx += 1
            if s_idx >= len(stress):
                Flag = True
                break
        if Flag:
            break
    
    return answer