def solution(X, Y):
    answer = []
    num_dic ={str(i):[0,0] for i in range(10)}
    xl, yl = len(X), len(Y)
    max_i = max(xl,yl)
    for i in range(max_i):
        if i < xl:
            num_dic[X[i]][0]+=1
        if i < yl:
            num_dic[Y[i]][1]+=1
    #print(num_dic)
    for j in range(9, 0, -1):
        m = min(num_dic[str(j)])
        answer.append([str(j)]*m)
    total = sum(answer,[])
    zeros = min(num_dic["0"])
    if len(total)==0:
        if zeros>0:
            return "0"
        else:
            return "-1"
    else:
        for _ in range(zeros):
            total.append("0")
        return "".join(total)
        
    return answer