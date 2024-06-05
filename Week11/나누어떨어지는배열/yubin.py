from itertools import filterfalse
def solution(arr, divisor):
    answer = list(filterfalse(lambda x: x%divisor, arr))
    if len(answer)>0:
        return sorted(answer)
    return [-1]