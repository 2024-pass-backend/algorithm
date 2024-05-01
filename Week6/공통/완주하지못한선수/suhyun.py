# 딕셔너리.get(키, 넣을 값) + 1
def solution(participant, completion):
    answer = ''
    part = dict()
    for p in participant:
        part[p] = part.get(p, 0) + 1
    
    # print(part)
    for c in completion:
        part[c] -= 1
    
    # print(part)
    for pp in part.keys():
        if part[pp] != 0:
            answer = pp
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))