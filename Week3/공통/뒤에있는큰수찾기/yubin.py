def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, num in enumerate(numbers):
        while stack:
            i, n = stack.pop()
            if num > n:
                answer[i] = num
            else:
                stack.append((i, n))
                break
        stack.append((idx, num))
    return answer

from collections import deque, defaultdict
def solution_old(numbers):
    answer = deque([])
    bigger = defaultdict(list)
    for i in range(len(numbers)):
        if len(answer)==0:
            answer.append(-1)
        else:
            n = numbers[~i]
            in_num = numbers[~(i-1)]
            if n<in_num:
                answer.appendleft(in_num)
                bigger[n].append(in_num)
            else:
                while True:
                    if bigger[in_num]:
                        in_num = bigger[in_num][-1]
                        if n<in_num:
                            answer.appendleft(in_num)
                            bigger[n].append(in_num)
                            break
                    else:
                        answer.appendleft(-1)
                        break
    return list(answer)