from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list) # 딕셔너리를 모든 키의 값을 빈 리스트로 초기화
    for info in information:
        info = info.split()
        condition = info[:-1] # 점수빼고 나머지 반환, 반환유형은 리스트. 왜냐, info자체가 리스트였기때문
        score = int(info[-1]) # 가장 맨뒤에 있는 원소에 접근하기 위해 info[-1] -1인덱스로 접근
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            print(case)
            for c in case:
                tmp = condition.copy() #얕은복사, 점수를 뺀 나머지 복사
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                print(f'key = {key}') # f'' > ''은 문자열로 이루어져있음
                dic[key].append(score)
                
    print(dic)
    
    for value in dic.values():
        value.sort()
        
    for query in queries:
        query = query.replace("and", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        
        if target_key in dic:
            target_list = dic[target_key]
            print("target_list")
            print(target_list)
            idx = bisect_left(target_list, target_score)
            print(idx)
            count = len(target_list) - idx
        answer.append(count)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))