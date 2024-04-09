from collections import deque, defaultdict
def solution(numbers):
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