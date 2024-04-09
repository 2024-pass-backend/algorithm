# numbers 길이가 1,000,000(백만) 
# 순차탐색을 진행하면 백만*백만으로 1초안에 풀 수 없을 듯하다.
# 따라서, 이분탐색으로 진행하자.
# ans = numbers후, ans만 정렬해주었는데도 내부적으로 ans와 numbers가 정렬되어있다.
# ans만 정렬시키도록 하기 위해 파이썬에서는 깊은 복사를 제공한다.
# import copy, a = copy.deepcopy(복사하고자 하는 배열)
# 9:20 ~ 9:40 오잉? 이 문제 어케 푸는거임? -> 이분탐색으로 접근하려고했다가 접근실패를 직감함.
# 결국 답을 확인하였다.
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = [0] # 스택 초기화
    
    for i in range(1, n):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer

print(solution([9, 1, 5, 3, 6, 2]))