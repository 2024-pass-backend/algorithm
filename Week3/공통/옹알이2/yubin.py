from collections import defaultdict
def solution(babbling):
    answer = 0
    
    four = ['aya', 'ye', 'woo', 'ma']
    dic = defaultdict(tuple)
    for w in four:
        dic[w[0]] = (len(w), w)
    
    for bab in babbling:
        idx = 0
        w='z'
        Flag = True
        while idx < len(bab):
            # 다음 위치 == 이번 첫 글자 -> 연달아 같은 발음 불가
            if bab[idx] == w[0]:
                Flag = False
                break
            if dic[bab[idx]]:
                l, w = dic[bab[idx]] # 길이, 발음 꺼내오기
                # 할 수 있는 발음이랑 동일
                if bab[idx:idx+l] == w: 
                    idx += l 
                # 할 수 있는 발음 아님
                else:
                    Flag = False
                    break
            # 할 수 있는 발음과 동일한 시작이 아님
            else:
                Flag = False
                break
        if Flag:
            answer += 1
    return answer