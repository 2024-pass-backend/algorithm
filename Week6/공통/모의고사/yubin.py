from itertools import cycle
def solution(answers):
    answer = []
    supo1 = cycle([1,2,3,4,5])
    supo2 = cycle([2,1,2,3,2,4,2,5])
    supo3 = cycle([3,3,1,1,2,2,4,4,5,5])
    
    score = [0, 0, 0]
    for ans, s1, s2, s3 in zip(answers, supo1, supo2, supo3):
        if s1==ans:
            score[0] += 1
        if s2==ans:
            score[1] += 1
        if s3==ans:
            score[2] += 1
    
    max_score = max(score)

    for idx, supo in enumerate(score):
        if supo==max_score:
            answer.append(idx+1)
    return answer