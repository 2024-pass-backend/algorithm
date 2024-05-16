# 문자열.split()의 반환값은 리스트이다.
def solution(info, query):
    answer = []
    for q in query:
        q = q.replace("and", "")
        print(q)
        q = q.split()
        print(q)
        count = 0
        for i in info:
            i = i.split()
            print(i)
            flag = True
            if int(i[4]) < int(q[4]):
                flag = False
            else:
                for idx in range(4):
                    if q[idx] == '-':
                        continue
                    else:
                        if q[idx] != i[idx]:
                            flag = False
                            break
            
            if flag:
                count += 1
        answer.append(count)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))