def solution(name, yearning, photo):
    answer = []
    miss_score = {n:s for n, s in zip(name, yearning)}
    for p in photo:
        temp = 0
        for person in p:
            if person in miss_score.keys():
                temp += miss_score[person]
        answer.append(temp)
    return answer