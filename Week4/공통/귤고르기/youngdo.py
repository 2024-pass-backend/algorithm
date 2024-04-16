def solution(k, tangerine):
    answer = 0
    dict = {}
    for i in tangerine:
        if (i in dict):
            dict[i] += 1
        else:
            dict[i] = 1
    dic = sorted(dict.items(), key=lambda x: x[1], reverse=True) #개수 많은거부터 추가하기 위해 정렬


    for i in dic:
        k -= i[1]
        answer += 1
        if (k <= 0):
            break

    return answer
