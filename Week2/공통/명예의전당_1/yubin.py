def solution(k, score):
    answer = []
    k_score = []
    for s in score:
        if len(k_score)<k:
            k_score.append(s)
            k_score = sorted(k_score)
        else:
            if s > k_score[0]:
                k_score[0] = s
                k_score = sorted(k_score)
        answer.append(k_score[0])
    return answer