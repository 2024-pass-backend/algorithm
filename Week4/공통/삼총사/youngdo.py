from itertools import combinations
def solution(number):
    # 조합으로 3개 짜기
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer
## 조합을 이용하지 않는 경우 3중 for문
# def solution(number):
#     answer = 0
#     l = len(number)
#     for i in range(l):
#         for j in range(i+1, l):
#             for k in range(j+1, l):
#                 if number[i] + number[j] + number[k] == 0:
#                     answer += 1
#     return answer