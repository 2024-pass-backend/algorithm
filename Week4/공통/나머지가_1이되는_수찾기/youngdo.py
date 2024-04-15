# def solution(n):
#     answer = 0
#     for i in range(1,n):
#         if n%i==1:
#             answer=i
#             break
#     return answer

def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer