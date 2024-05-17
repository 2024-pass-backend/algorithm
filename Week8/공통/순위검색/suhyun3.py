from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(information, queries):
    answer = []
    dic = defaultdict(list) # 딕셔너리의 모든 키의 값을 빈리스트로 초기화
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])

        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score)

    for value in dic.values():
        value.sort()

    # print(dic)

    for query in queries:
        query = query.replace("and", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0

        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))